from pymongo import MongoClient
import csv  #facilitates CSV I/O

#server = MongoClient("localhost")
server = MongoClient("lisa.stuy.edu")
ourDB = server['bagels']


def makeStudentColl():
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

def makeTeacherColl():
    f = open("teachers.csv")
    teacherList = csv.DictReader(f)
    for teacher in teacherList:
        doc = {}
        doc['name'] = teacher['teacher']
        doc['class'] = teacher['code']
        doc['period'] = teacher['period']
        doc['students'] = []

        students = ourDB.students.find()
        
        for student in students:
            courses = student['courses']
            for course in courses:
                if course['code'] == doc['class']:
                    doc['students'].append(student['id'])
                    break

        ourDB.teachers.insert_one(doc)

makeStudentColl()
makeTeacherColl()


