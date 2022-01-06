import requests

from create_user import URL, USER_DATA

def update_user():
    USER_DATA["hobbies"]= "Shooting"
    out = requests.put(URL+"/1", json=USER_DATA)
    if out.status_code == 200:
        print("Updated")
    else:
        print("Something went wrong.")

if __name__ == "__main__":
    update_user()
