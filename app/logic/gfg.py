# gfg.py
import requests
from bs4 import BeautifulSoup

def scrape_gfg_problems(limit=100):
    print("Scraping GFG problems...")
    url = "https://www.geeksforgeeks.org/tag/arrays/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        print("GFG page fetched.")
        print("Preview of page:", soup.title.text)
    except Exception as e:
        print("GFG fetch error:", e)
        return []

    problems = []
    articles = soup.select("div.tag-site-section article")

    print(f"Found {len(articles)} problem links")

    for i, article in enumerate(articles):
        if i >= limit:
            break
        a = article.find("a")
        if not a:
            continue
        title = a.text.strip()
        link = a['href']
        problems.append({
            "title": title,
            "difficulty": "unknown",
            "platform": "GFG",
            "topics": ["arrays"],
            "url": link
        })

    print(f"Total GFG problems scraped: {len(problems)}")
    return problems
