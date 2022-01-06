import requests

USER_DATA = {
    "first_name": "Test",
    "last_name": "User",
    "hobbies": "Test hobby"
}

URL = "http://127.0.0.1:5000/users"

def create_user():
    out = requests.post(URL, json=USER_DATA)
    if out.status_code == 201:
        print("OK")
    else:
        print("Something went wrong.")

if __name__ == "__main__":
    create_user()