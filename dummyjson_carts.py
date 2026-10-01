import requests
import pandas as pd

url = "https://dummyjson.com/carts"

limit = 20
skip = 0

product_records = []

while True:
    params = {
        "limit": limit,
        "skip": skip
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    for cart in data["carts"]:
        for product in cart["products"]:
            record = {
                "cart_id": cart["id"],
                "user_id": cart["userId"],
                "product_id": product["id"],
                "title": product["title"],
                "price": product["price"],
                "quantity": product["quantity"],
                "total": product["total"],
                "discount_percentage": product["discountPercentage"],
                "discounted_total": product["discountedTotal"]
            }

            product_records.append(record)

    skip += limit

    if skip >= data["total"]:
        break

df = pd.DataFrame(product_records)
df.to_csv("carts.csv", index=False)

print(len(df))
