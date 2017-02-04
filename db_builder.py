from pymongo import MongoClient
import csv  #facilitates CSV I/O

#server = MongoClient("localhost")
server = MongoClient("lisa.stuy.edu")
ourDB = server['bagels']

peeps = open("peeps.csv")
courses = open("courses.csv")

people = csv.DictReader(peeps)
courseList = csv.DictReader(courses)

for person in people:
    oneStudent = {} #the document
    oneStudent['name'] = person['name']
    oneStudent['age'] = person['age']
    oneStudent['id'] = person['id']

    #create list of courses & grades for this student
    grades = []
    for course in courseList:
        if course['id'] == oneStudent['id']:
            grades.append( { 'code' : course['code'], 'mark' : course['mark'] } )
    oneStudent['courses'] = grades

    #reset "cursor" of file to beginning
    #allows iteration through courseList again
    courses.seek(0)
    
    #put doc into students collection
    ourDB.students.insert_one(oneStudent) 




