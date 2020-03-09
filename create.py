import csv
from application import db
from application.models import Userteams, Users, Players

db.drop_all()
db.create_all()

#with open('players.csv') as playaz:
#    csv_reader = csv.reader(playaz, delimiter=",")
#    line_count=0
#    for row in csv_reader:
#        if line_count==0:
#            line_count+=1
#        else:
#            db.session.add(Players(
#                name = row[1],
#                club = row[2],
#                position = row[4]
#            ))
#            db.session.commit()