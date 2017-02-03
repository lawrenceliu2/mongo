import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...


q = "CREATE TABLE students (name TEXT, id INTEGER);"
c.execute(q)    #run SQL query
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER);"
c.execute(q)


fObj1 = open("peeps.csv")
d = csv.DictReader(fObj1) 
for row in d:
    insertion = "INSERT INTO students VALUES (\"" + row["name"] + "\", " + row["id"] + ")" #Adds each name and ID into the students table
    c.execute(insertion)

fObj2 = open("courses.csv")
e = csv.DictReader(fObj2)
for row in e:
    insertion = "INSERT INTO courses VALUES (\"%s\", %s, %s)" % (row["code"], row["id"], row["mark"]) #Adds each course, id, and grade into the courses table
    c.execute(insertion)


#==========================================================
db.commit() #save changes
db.close()  #close database
