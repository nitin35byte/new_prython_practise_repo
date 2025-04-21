import time
from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url = "https://www.flipkart.com"
search_url = "/search?q=smart+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&as-pos=2&as-type=RECENT&suggestionId=smart+phone%7CMobiles&requestId=633dab26-76ac-4771-9b75-74c92a8232ed&as-searchtext=smart%20phone"
visited_links = set()
url = base_url + search_url
counter = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

while counter < 10:  # Scraping up to 10 pages
    print(f"Scraping page {counter + 1} - URL: {url}")
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 429:
        print("Received 'Too Many Requests' error. Waiting before retrying...")
        time.sleep(10)  # Wait for 10 seconds and retry
        continue
    soup = BeautifulSoup(response.text, 'html.parser')

    products_data = []

    # Find all product cards
    postings = soup.find_all('div', class_='cPHDOP col-12-12')

    if not postings:
        print("No product postings found. Check if the CSS selector '-' is still valid.")
        break

    for post in postings:
        product_name_elem = post.find('div', class_='KzDlHZ')
        product_name = product_name_elem.text.strip() if product_name_elem else "Product Name Not Found"

        discounted_price_elem = post.find('div', class_='Nx9bqj _4b5DiR')
        product_selling_price = discounted_price_elem.text.strip() if discounted_price_elem else "Price Not Available"

        actual_price_elem = post.find('div', class_='yRaY8j ZYYwLA')
        product_actual_price = actual_price_elem.text.strip() if actual_price_elem else "Actual Price Not Available"

        rating_elem = post.find('div', class_='XQDdHH')
        user_rating = rating_elem.text.strip() if rating_elem else "Rating Not Available"

        ratings_reviews_elem = post.find('span', class_='Wphh3N')
        user_ratings_reviews = ratings_reviews_elem.text.strip() if ratings_reviews_elem else "Ratings & Reviews Not Available"

        specification_elem = post.find('div', class_='_6NESgJ')
        specification = specification_elem.text.strip() if specification_elem else "Specifications Not Available"

        # Append product data to a list of dictionaries
        product_data = {
            'Product Name': product_name,
            'Selling Price': product_selling_price,
            'Actual Price': product_actual_price,
            'User Rating': user_rating,
            'User Ratings & Reviews': user_ratings_reviews,
            'Specifications': specification
        }
        products_data.append(product_data)

    # Convert list of dictionaries to DataFrame for further analysis or output
    df = pd.DataFrame(products_data)
    print(df)
    visited_links.add(search_url)
    # Find next page URL and update `url` for the next iteration
    next_page = soup.find('a', class_='_9QVEpD')
    if not next_page:
        print("No next page link found.")
        break

    next_page_url = urljoin(base_url, next_page['href'])
    url = next_page_url

    counter += 1  # Increment the counter to track the number of pages scraped
df = pd.DataFrame(products_data)
output_file = 'mobiles.csv'
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} unique car listings to {output_file}")
