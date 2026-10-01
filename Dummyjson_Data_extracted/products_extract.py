import requests
import pandas as pd
import json


def main():

    base_url = "https://dummyjson.com"
    endpoint = "/products"

    limit = 30
    skip = 0

    all_products = []

    # Extract all pages
    while True:

        url = f"{base_url}{endpoint}?limit={limit}&skip={skip}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        products = data["products"]

        all_products.extend(products)

        skip += limit

        if skip >= data["total"]:
            break

    print("Total products:", len(all_products))

    # Select required fields
    product_data = []

    for product in all_products:
        product_data.append({
            "id": product["id"],
            "title": product["title"],
            "category": product["category"],
            "brand": product.get("brand"),
            "price": product["price"],
            "discountPercentage": product["discountPercentage"],
            "rating": product["rating"]
        })

    df =pd.DataFrame(product_data) 

    df.to_csv('products.csv',index= False)

    with open('products.json','w') as file:
        json.dump(product_data,file,indent=4)

print("Extracted data and saved successfully")

if __name__ == '__main__':
    main()
