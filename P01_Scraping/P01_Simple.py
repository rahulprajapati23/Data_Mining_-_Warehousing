import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Fetch data from Snapdeal
url = "https://www.snapdeal.com/search?keyword=mobiles&sort=rlvncy"
headers = {'User-Agent': 'Mozilla/5.0'}
print(f"Fetching data from {url}...")

try:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
except Exception as e:
    print(f"Error: {e}")
    exit()

# 2. Extract Product Info
names, prices = [], []
for prod in soup.find_all("div", class_="product-tuple-listing"):
    title = prod.find("p", class_="product-title")
    price = prod.find("span", class_="product-price")
    names.append(title.get('title', title.text.strip()) if title else "N/A")
    prices.append(price.text.strip() if price else "N/A")

# 3. Output Table and Save
if names:
    df = pd.DataFrame({"Product Name": names, "Price": prices})
    print("\n" + "="*50 + "\nFINAL OUTPUT\n" + "="*50)
    pd.set_option('display.max_rows', None, 'display.width', 1000)
    print(df)
    df.to_excel("Snapdeal_Mobiles_v2.xlsx", index=False)
    print(f"\nSaved to Snapdeal_Mobiles_v2.xlsx")
else:
    print("No products found.")
