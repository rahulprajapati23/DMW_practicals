# Practical 1: Web Scraping
# Extracted from DMW_Practical_source_code.py (Colab -> local)

# NOTE: Colab-specific magics and downloads have been converted for local use.
# If libraries are missing, install them in your environment, e.g. `pip install requests bs4 pandas`.

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

response = requests.get(url)
soap = BeautifulSoup(response.text, "html.parser")

names = []
descriptions = []
prices = []
ratings = []
reviews = []

products = soap.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")

for product in products:
    name = product.find("a", class_="title").text.strip()
    price = product.find("span", itemprop="price").text.strip()
    desc = product.find("p", itemprop="description").text.strip()
    div = product.find("div", class_="ratings")
    tag = div.find("p", attrs={"data-rating": True})
    rating = tag.get("data-rating")
    review = product.find("span", itemprop="reviewCount").text.strip()

    names.append(name)
    prices.append(price)
    descriptions.append(desc)
    ratings.append(rating)
    reviews.append(review)


data = {
    "Product Name": names,
    "Price (in €)": prices,
    "Specification": descriptions,
    "Rating": ratings,
    "Number of Reviews": reviews
}

if names:
    df = pd.DataFrame(data)
    print(df.head())
    out_path = "Prac1.xlsx"
    df.to_excel(out_path, index=False)
    print(f"Saved output to {out_path}")
else:
    print("No products found. Check the target URL or selectors.")
