import requests
from random import choice

UPDATE_USER = {
    "first_name": "Gary",
    "last_name" : "Galvin",
    "hobbies": choice(
        [
            "Driving",
            "Hunting",
            "Fishing",
            "Legos",
            "Models",
            "Wood Working",
            "Fitness",
            "Movies"
        ]
    )
}

URL = "http://127.0.0.1:5000/users/1"

def update_user():
    out = requests.put(URL, json=UPDATE_USER)
    if out.status_code == 200:
        print("Update successful.")
    else:
        print("Update failed")

if __name__ == "__main__":
    update_user()
