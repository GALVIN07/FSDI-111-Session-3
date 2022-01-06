import requests

from create_user import URL, USER_DATA

def deactivate_user():
    USER_DATA["first_name"] = "Bob"
    out = requests.delete(URL+"/2", json=USER_DATA)
    if out.status_code == 200:
        print("User Successfully Deleted")
    else: 
        print("Something went wrong")


if __name__ == "__main__":
    deactivate_user()