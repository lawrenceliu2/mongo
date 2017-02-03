from pymongo import MongoClient
import csv       #facilitates CSV I/O

server = MongoClient("lisa.stuy.edu")
ourDB = server['bagels']

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...



oneStudent = {}

fObj1 = open("peeps.csv")
d = csv.DictReader(fObj1)

for row in d:
    oneStudent['name'] = row['name']
    oneStudent['age'] = row['age']
    oneStudent['id'] = row['id']
    print oneStudent
    oneStudent = {}


fObj2 = open("courses.csv")
e = csv.DictReader(fObj2)
