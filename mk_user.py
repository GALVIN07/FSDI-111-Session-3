from app import db, User

def create_user(first_name, last_name, hobbies):
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()


if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    hobbies = input("Enter hobbies: ")
    create_user(first_name, last_name, hobbies)
    user = User.query.all()
    opt = input("show Users? [y/n]: ")
    if opt == "y":
        users = User.query.all()
        print(users)