import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

def extract_data(config):
    response = requests.get(config['url'])
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.select(config['item_selector'])

    data = []
    for item in items:
        row = {}
        for field, selector in config['fields'].items():
            if '@' in selector:
                sel, attr = selector.split('@')
                tag = item.select_one(sel)
                row[field] = tag[attr] if tag and tag.has_attr(attr) else None
            else:
                tag = item.select_one(selector)
                row[field] = tag.get_text(strip=True) if tag else None
        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv(config['output'], index=False)
    print(f"✅ Data exported to {config['output']}")

if __name__ == "__main__":
    with open('config.json') as f:
        config = json.load(f)
    extract_data(config)