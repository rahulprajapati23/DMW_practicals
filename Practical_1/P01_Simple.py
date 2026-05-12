# Practical 1: Web Scraping - Simple Version

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")

data = []
for product in products:
    name = product.find("a", class_="title").text.strip()
    price = product.find("span", itemprop="price").text.strip()
    desc = product.find("p", itemprop="description").text.strip()
    rating = product.find("p", attrs={"data-rating": True}).get("data-rating")
    reviews = product.find("span", itemprop="reviewCount").text.strip()
    
    data.append({
        "Product Name": name,
        "Price (in €)": price,
        "Specification": desc,
        "Rating": rating,
        "Number of Reviews": reviews
    })

df = pd.DataFrame(data)
print(df)
df.to_excel("Prac1.xlsx", index=False)
