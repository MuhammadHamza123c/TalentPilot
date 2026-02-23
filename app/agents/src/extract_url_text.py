import requests
from bs4 import BeautifulSoup

def extract_portfolio_text(url: str, max_chars: int = 8000) -> str:
    try:
        # --- Step 1: Fetch webpage ---
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=40)
        response.raise_for_status()

        # --- Step 2: Parse HTML ---
        soup = BeautifulSoup(response.text, "html.parser")

        # --- Step 3: Remove unwanted tags ---
        for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
            tag.decompose()

        # --- Step 4: Extract text ---
        text = soup.get_text(separator=" ")

        # --- Step 5: Clean text ---
        lines = [line.strip() for line in text.split()]
        clean_text = " ".join(lines)

        # --- Step 6: Limit size for LLM ---
        return clean_text[:max_chars]

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching URL: {str(e)}")

