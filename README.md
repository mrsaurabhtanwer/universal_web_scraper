# 🌐 Universal Web Scraper (CSV Exporter)

A general-purpose, configuration-driven web scraping tool built for data scientists, analysts, and engineers. Easily extract structured data from websites using a simple JSON config file and export it to CSV for your projects.

## 🚀 Features
- Configurable: No hardcoding – change websites and elements using JSON
- Lightweight: Uses `requests` + `BeautifulSoup`
- CSV Export: Outputs structured data into `.csv`
- Dynamic Support: Optional Selenium module for dynamic pages

## 🛠️ Dependencies
```
requests  
beautifulsoup4  
pandas  
selenium *(optional)*
```

Install via:
```bash
pip install -r requirements.txt
```

## ⚙️ How to Use

1. Edit `config.json` to set your website, selectors, and output path.
2. Run the script:

```bash
python scraper.py --config config.json
```

## 🧪 Example Config
```json
{
  "url": "https://books.toscrape.com/",
  "item_selector": ".product_pod",
  "fields": {
    "title": "h3 a@title",
    "price": ".price_color",
    "availability": ".availability"
  },
  "output": "output/books_data.csv"
}
```

---

## 🧠 Supported Use Cases
- 📚 Book listings
- 💼 Job postings
- 📰 News headlines
- 💬 Product reviews
- 🎬 Movie data
- And more!