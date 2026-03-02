import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_snapdeal():
    url = "https://www.snapdeal.com/search?keyword=mobiles&sort=rlvncy"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print(f"Fetching data from {url}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    product_names = []
    prices = []
    
    products = soup.find_all("div", class_="product-tuple-listing")
    print(f"Found {len(products)} products. Processing...\n")
    
    for product in products:
        try:
            title_tag = product.find("p", class_="product-title")
            title = title_tag['title'] if title_tag else product.find("p", class_="product-title").text.strip()
            
            price_tag = product.find("span", class_="product-price")
            price = price_tag.text.strip() if price_tag else "N/A"
            
            product_names.append(title)
            prices.append(price)
            
        except Exception as e:
            continue

    if product_names:
        df = pd.DataFrame({
            "Product Name": product_names,
            "Price": prices
        })
        
        # --- This produces the "Output like this" format ---
        print("\n" + "="*80)
        print("FINAL OUTPUT TABLE")
        print("="*80)
        
        # Adjust pandas settings to print the full table nicely
        pd.set_option('display.max_rows', None)      # Show all rows
        pd.set_option('display.max_columns', None)   # Show all columns
        pd.set_option('display.width', 1000)         # Prevent wrapping
        pd.set_option('display.max_colwidth', 60)    # Truncate long titles slightly if needed
        pd.set_option('display.expand_frame_repr', False) # Don't wrap to new lines
        
        print(df)
        print("="*80)
        # ----------------------------------------------------
        
        output_file = "Snapdeal_Mobiles_v2.xlsx"
        df.to_excel(output_file, index=False)
        print(f"\nData successfully saved in {output_file}")
    else:
        print("No products found. Css selectors might need adjustment.")

if __name__ == "__main__":
    scrape_snapdeal()
