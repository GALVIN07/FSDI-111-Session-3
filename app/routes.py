import requests
from flask import request
from datetime import datetime

from app import app, db
from app.database import User

VERSION = "1.0.0"

@app.get("/version")
def get_version():
    out = {}
    out["server_time"] = (
        datetime.now().strftime("%F %H:%M:%S"))
    out["version"] = VERSION
    return out




@app.post("/users")
def creat_user():
    user_data = request.json
    db.session.add(
        User(
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            hobbies=user_data.get("hobbies")
        )
    )
    db.session.commit()
    return {"status": "success"}, 201

@app.get("/users")
def get_all_users():
    users = User.query.all()
    out_list = []
    for user in users:
        temp = {}
        temp["first_name"]= user.first_name
        temp["last_name"] = user.last_name
        temp["hobbies"] = user.hobbies
        temp["active"] = user.active
        out_list.append(temp)
    return {"users": out_list}

# @app.get("/users/<int:pk>")
# def get_single_user(pk):
#     user_record = user.read(pk)
#     out = {"user": user_record}
#     return out

# @app.put("/users/<int:pk>")
# def put_single_user(pk):
#     user_data = request.json
#     user.update(
#     pk,
#     user_data.get("first_name"),
#     user_data.get("last_name"),
#     user_data.get("hobbies")
#     )

#     return "ok", 204
    


# @app.delete("/users/<int:pk>")
# def delete_single_user(pk):
#     user.deactivate_user(pk) 

#     return "OK", 204

# FOR UPDATE: an HTTP PUT operation with rout: /users/<int:pk> 
# FOR DEACTIVATE: an HTTP DELETE operation with route: /user/<int:pk>