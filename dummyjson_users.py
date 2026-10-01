import requests
import pandas
import json

def main():
    url = "https://dummyjson.com/users"

    limit = 30 
    skip =0 

    all_users = []
    while True:
        url = f"https://dummyjson.com/users?limit={limit}&skip={skip}"
        response = requests.get(url)

        response.raise_for_status
        data = response.json() 

        users = data["users"]

        all_users.extend(users)

        skip = skip+limit

        if skip>= data["total"]:
            break
    print("Total_users",len(all_users))

    user_data = []

    for user in users:
        user_data.append({
            "id": user["id"],
            "firstName" : user["firstName"],
            "lastName"  : user["lastName"],
            "gender"    : user["gender"],
            "address"   : user["address"]["address"],
            "city"      : user["address"]["city"],
            "state"     : user["address"]["state"],
            "statecode" : user["address"].get("stateCode"),
            "country"   : user["address"]["country"]
        })

    with open("users.json","w") as file:
        json.dump(user_data,file,indent=4)

    print("extraced and saved successfully ")

if __name__ == "__main__":
    main()
