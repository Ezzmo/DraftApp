import csv
from application import db, bcrypt
from application.models import Userteams, Users, Players

db.drop_all()
db.create_all()

db.session.add(Users(
    name = "admin",
    password = bcrypt.generate_password_hash("admin")

))
db.session.commit()
with open('players.csv') as playaz:
    csv_reader = csv.reader(playaz, delimiter=",")
    line_count=0
    for row in csv_reader:
        if line_count==0:
            line_count+=1
        else:
            db.session.add(Players(
                name = row[1],
                age = row[2],
                position = row[5]
            ))
            db.session.commit()