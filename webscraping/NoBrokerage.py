import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=smart+phone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&as-pos=2&as-type=RECENT&suggestionId=smart+phone%7CMobiles&requestId=633dab26-76ac-4771-9b75-74c92a8232ed&as-searchtext=smart%20phone"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
##print(soup)
postings=soup.find_all('div',class_='cPHDOP col-12-12')
for post in postings:
    ##link= post.find('a',class_='CGtC98')['href']
    name=post.find('div',class_='KzDlHZ')
    if name:
        product_name = name.text.strip()
        ##print(product_name)
    else:
        pass

    discounted_price=post.find('div',class_='Nx9bqj _4b5DiR')
    if discounted_price:
        product_selling_price = discounted_price.text
        ##print(product_selling_price)
    else:
        pass

    actual_price=post.find('div',class_='yRaY8j ZYYwLA')
    if actual_price:
        product_actual_price = actual_price.text
        ##print(product_actual_price)
    else:
        pass

    rating=post.find('div',class_='XQDdHH')
    if rating:
        user_rating = rating.text.strip()
        ##print(user_rating)
    else:
        pass


    ratings_reviews=post.find('span',class_='Wphh3N')
    if ratings_reviews:
        user_ratings_reviews = ratings_reviews.text.strip()
        print(user_ratings_reviews)
    else:
        pass

    specification=post.find('div',class_='_6NESgJ')

    if specification:
        specification = specification.text.strip()
        print(specification)
    else:
        pass


print(product_name,product_selling_price,product_actual_price,user_rating,user_ratings_reviews,specification)

