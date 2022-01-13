
from flask import request, render_template
from datetime import datetime

from app import app, db
from app.database import User

VERSION = "1.0.0"

@app.get("/")
def get_home():
    return render_template("home.html")


@app.get("/about")
def get_about():
    return render_template("about.html")
    

@app.get("/version")
def get_version():
    out = {}
    out["server_time"] = (
        datetime.now().strftime("%F %H:%M:%S"))
    out["version"] = VERSION
    return out


@app.post("/users")
def create_user():
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
        temp["id"] = user.id
        temp["first_name"]= user.first_name
        temp["last_name"] = user.last_name
        temp["hobbies"] = user.hobbies
        temp["active"] = user.active
        out_list.append(temp)
    return render_template("list_users.html", users=out_list)

@app.get("/users/<int:pk>")
def get_single_user(pk):
    user = User.query.filter_by(id=pk).first()
    return render_template("user_detail.html", user=user)

@app.put("/users/<int:pk>")
def update_user(pk):
    user_data = request.json
    user = User.query.filter_by(id=pk).first()
    user.first_name = user_data.get("first_name", user.first_name)
    user.last_name = user_data.get("last_name", user.last_name)
    user.hobbies = user_data.get("hobbies", user.hobbies)
    user.active = user_data.get("active", user.active)
    db.session.commit()
    return {"status": "success"}, 200
    


@app.delete("/users/<int:pk>/soft")
def deactivate_user(pk):
    user = User.query.filter_by(id=pk).first()
    user.active = 0
    db.session.commit()

    return {"status" : "succcess"}


@app.delete("/user/<int:pk>/permanent")
def delete_user(pk):
    User.query.filter_by(id=pk).delete()
    db.session.commit()
    return {"status": "success"}

# FOR UPDATE: an HTTP PUT operation with rout: /users/<int:pk> 
# FOR DEACTIVATE: an HTTP DELETE operation with route: /user/<int:pk>