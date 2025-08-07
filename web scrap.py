import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"  # Change to any public news site
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    
    for h2 in soup.find_all('h2'):
        text = h2.get_text(strip=True)
        if text:
            headlines.append(text)
    
    page_title = soup.title.string if soup.title else None
    if page_title:
        headlines.insert(0, page_title)

    with open("news_headlines.txt", "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")
    
    print(f"✅ {len(headlines)} headlines saved to 'news_headlines.txt'")
else:
    print(f"❌ Failed to fetch page. Status code: {response.status_code}")
