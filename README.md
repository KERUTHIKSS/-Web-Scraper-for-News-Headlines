# 📰 Web Scraper for News Headlines

This is a simple Python project to **automate the collection of news headlines** from a public website using web scraping techniques. It uses `requests` to fetch HTML content and `BeautifulSoup` to parse the HTML and extract news titles from `<h2>` or `<title>` tags. The headlines are saved into a `.txt` file.

---

## ✅ Features

- Fetches live HTML content from a news website
- Parses and extracts headlines from `<h2>` and `<title>` tags
- Saves headlines into a plain text file
- Easy to modify for different websites or tags

---

## 🧠 Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/) – for making HTTP requests
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) – for parsing HTML

---

## 🚀 How to Run

1. **Install dependencies**

```bash
pip install requests beautifulsoup4
