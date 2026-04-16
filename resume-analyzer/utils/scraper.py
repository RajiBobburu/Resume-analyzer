import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(resp.text, "html.parser")

        for tag in soup(["script", "style"]):
            tag.decompose()

        return soup.get_text(separator="\n")[:5000]

    except Exception as e:
        return str(e)