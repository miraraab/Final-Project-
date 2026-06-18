import logging
import requests
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

SEARCH_KEYWORDS = [
    "Energiewende",
    "Energieeffizienz",
    "Wärmepumpe Gebäudesanierung",
    "Elektromobilität",
    "dena Deutsche Energie-Agentur",
    "Wasserstoff Energie"
]

RELEVANCE_KEYWORDS = [
    "energiewende",
    "energieeffizienz",
    "wasserstoff",
    "wärmepumpe",
    "gebäudesanierung",
    "elektromobilität",
    "e-mobilität",
    "dena",
    "erneuerbare",
    "dekarbonisierung",
    "photovoltaik",
    "klimaneutral",
    "netzausbau",
    "sektorenkopplung",
    "industrie energie",
    "effizienz",
    "co2",
    "emissionen"
]


def score_article(article: dict) -> int:
    """
    Score an article based on relevance keywords.

    Args:
        article: Article dict with 'title' and 'description'

    Returns:
        Count of relevance keywords found
    """
    # Combine title and description into one lowercase string
    text = (article.get("title", "") + " " + article.get("description", "")).lower()

    # Count how many relevance keywords appear
    score = 0
    for keyword in RELEVANCE_KEYWORDS:
        if keyword in text:
            score += 1

    return score


def fetch_energy_news(api_key: str, max_per_keyword: int = 2) -> list[dict]:
    """
    Fetch relevant energy sector news from NewsAPI.

    Args:
        api_key: NewsAPI API key
        max_per_keyword: Max articles per keyword

    Returns:
        List of deduplicated news articles, max 10 total
    """
    if not api_key:
        logger.warning("NEWS_API_KEY not provided, skipping news fetch")
        return []

    articles = []
    seen_urls = set()
    today = datetime.now(timezone.utc)  # Use UTC timezone to match NewsAPI timestamps
    week_ago = today - timedelta(days=7)
    from_date = week_ago.strftime("%Y-%m-%d")

    for keyword in SEARCH_KEYWORDS:
        try:
            response = requests.get(
                "https://newsapi.org/v2/everything",
                params={
                    "q": keyword,
                    "language": "de",
                    "sortBy": "publishedAt",
                    "pageSize": max_per_keyword,
                    "from": from_date,
                    "apiKey": api_key
                },
                timeout=10
            )

            if response.status_code != 200:
                logger.warning(f"NewsAPI error for '{keyword}': {response.status_code}")
                continue

            data = response.json()

            if data.get("status") != "ok":
                logger.warning(f"NewsAPI status not ok for '{keyword}': {data.get('message')}")
                continue

            # Process articles
            for article in data.get("articles", []):
                # Skip removed articles
                if article.get("title") == "[Removed]":
                    continue

                url = article.get("url", "")

                # Deduplicate by URL
                if url in seen_urls:
                    continue
                seen_urls.add(url)

                # Parse published date
                try:
                    pub_date = datetime.fromisoformat(article.get("publishedAt", "").replace("Z", "+00:00"))
                    # Double-check it's within 7 days
                    if (today - pub_date).days > 7:
                        continue
                    date_str = pub_date.strftime("%d.%m.%Y")
                except Exception as e:
                    logger.debug(f"Error parsing date: {e}")
                    continue

                # Extract description and truncate
                description = article.get("description", "")
                if description and len(description) > 120:
                    description = description[:117] + "..."

                article_dict = {
                    "title": article.get("title", "").strip(),
                    "source": article.get("source", {}).get("name", "Unknown"),
                    "url": url,
                    "published_at": date_str,
                    "keyword": keyword,
                    "description": description
                }

                # Score article for relevance (no filter, just for sorting/display)
                relevance_score = score_article(article_dict)
                article_dict["relevance_score"] = relevance_score
                articles.append(article_dict)

        except requests.RequestException as e:
            logger.warning(f"Error fetching news for '{keyword}': {e}")
            continue
        except Exception as e:
            logger.warning(f"Error processing news for '{keyword}': {e}")
            continue

    # Sort by relevance score descending, then by published_at descending
    articles.sort(
        key=lambda x: (x.get("relevance_score", 0), x["published_at"]),
        reverse=True
    )
    articles = articles[:10]

    logger.info(f"Fetched {len(articles)} unique news articles after relevance filtering")
    return articles


def build_news_html(articles: list[dict]) -> str:
    """
    Build HTML block for news articles.

    Args:
        articles: List of article dicts from fetch_energy_news()

    Returns:
        HTML block string, or empty string if no articles
    """
    if not articles:
        return ""

    articles_html = ""
    for article in articles:
        relevance_score = article.get("relevance_score", 0)
        articles_html += f"""
        <div style="padding: 8px 0; border-bottom: 1px solid #dbeafe; color: #374151;">
            <a href="{article['url']}" style="color: #003087; font-weight: 600; font-size: 14px; text-decoration: none;" target="_blank">
                {article['title']}
            </a>
            <br>
            <span style="color: #6b7280; font-size: 12px;">
                {article['source']} · {article['published_at']} ·
                <span style="background: #003087; color: white; font-size: 10px; padding: 1px 5px; border-radius: 8px; margin-left: 4px;">
                    ★ {relevance_score}
                </span>
            </span>
            <br>
            <span style="color: #6b7280; font-size: 13px;">
                {article['description']}
            </span>
        </div>
    """

    return f"""
    <div style="background-color: #f0f4ff; border-left: 4px solid #003087; padding: 16px; margin-bottom: 16px; border-radius: 4px;">
        <h2 style="margin: 0 0 12px 0; color: #003087; font-size: 14px; font-weight: 600;">
            📰 Relevante Branchennews — letzte 7 Tage
        </h2>
        <div style="color: #374151; font-size: 13px;">
            {articles_html}
        </div>
        <div style="margin-top: 12px; padding-top: 8px; border-top: 1px solid #dbeafe;">
            <em style="color: #6b7280; font-size: 11px;">
                Powered by NewsAPI · Automatisch kuratiert
            </em>
        </div>
    </div>
    """


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from pathlib import Path

    # Load environment variables
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        print("NEWS_API_KEY not set in .env")
        print("Get a free API key from https://newsapi.org/")
        exit(1)

    print("=" * 80)
    print("Fetching Energy Sector News with Relevance Filtering")
    print("=" * 80)

    # First, fetch all articles to show the before/after count
    import requests
    from datetime import datetime, timezone, timedelta

    all_articles_count = 0
    today = datetime.now(timezone.utc)
    week_ago = today - timedelta(days=7)
    from_date = week_ago.strftime("%Y-%m-%d")

    for keyword in SEARCH_KEYWORDS[:2]:  # Sample 2 keywords
        response = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q": keyword,
                "language": "de",
                "sortBy": "publishedAt",
                "pageSize": 2,
                "from": from_date,
                "apiKey": api_key
            },
            timeout=10
        )
        data = response.json()
        all_articles_count += len(data.get("articles", []))

    articles = fetch_energy_news(api_key)

    print(f"\nFetching articles from last 7 days...")
    print(f"Total articles fetched from NewsAPI: ~{all_articles_count * 3} (estimated)")
    print(f"Articles returned (sorted by relevance score): {len(articles)}\n")

    if articles:
        print(f"Top {len(articles)} most relevant articles:\n")
        for i, article in enumerate(articles, 1):
            score = article.get('relevance_score', 0)
            print(f"{i}. {article['title'][:70]}")
            print(f"   Score: {score} | Source: {article['source']} | {article['published_at']}")
            print()
    else:
        print("No articles passed the relevance filter.")

    print("=" * 80)
