import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def run_web_scraper():
    print("==================================================")
    print("         CODEALPHA AUTOMATED WEB SCRAPER          ")
    print("==================================================")
    
    # Target URL: Public sandbox site designed for scrapers
    target_url = "http://quotes.toscrape.com/"
    
    # Configure request headers to mimic a genuine browser session
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"[SYSTEM] Sending HTTP GET request to: {target_url}...")
    try:
        response = requests.get(target_url, headers=headers, timeout=10)
    except Exception as e:
        print(f"\n[ERROR] Connection failed: {e}")
        return

    if response.status_code == 200:
        print("✔ Connection successful (HTTP 200 OK). Parsing HTML tree...")
        
        # Initialize BeautifulSoup parser
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Temporary storage blocks for the custom dataset
        scraped_records = []
        
        # Locate all quote content blocks on the page
        quote_elements = soup.find_all('div', class_='quote')
        print(f"✔ Found {len(quote_elements)} relevant data records on the page.")
        
        # Extract individual text elements
        for element in quote_elements:
            text = element.find('span', class_='text').text.replace('“', '').replace('”', '').strip()
            author = element.find('small', class_='author').text.strip()
            
            # Tag list extraction loop
            tags_meta = element.find('div', class_='tags').find_all('a', class_='tag')
            tags_list = [tag.text for tag in tags_meta]
            tags_string = ", ".join(tags_list)
            
            # Build dataset record
            scraped_records.append({
                "Quote Text": text,
                "Author": author,
                "Associated Tags": tags_string
            })
        
        # Convert into a structured pandas dataframe
        print("\n[SYSTEM] Compiling raw data arrays into a Pandas DataFrame...")
        df = pd.DataFrame(scraped_records)
        
        # Display the custom dataset preview in the terminal console window
        print("\n--- Structured Custom Dataset Preview ---")
        print(df.to_string(index=False, max_colwidth=40))
        print("-" * 50)
        
        # Exporting data out to CSV
        output_filename = "custom_scraped_dataset.csv"
        df.to_csv(output_filename, index=False, encoding='utf-8')
        print(f"✔ SUCCESS: Dataset exported smoothly to file -> '{output_filename}'")
        
    else:
        print(f"❌ Failed to retrieve page. Server returned status code: {response.status_code}")

    print("==================================================")

if __name__ == "__main__":
    run_web_scraper()