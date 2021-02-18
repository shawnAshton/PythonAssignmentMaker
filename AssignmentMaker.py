# LA's get backups... brit print and one to post
# birthday.. Phone num...print by month
import calendar
import datetime
from datetime import date
from datetime import date, timedelta
# CLASSES
class Person:
  def __init__(self, f, l):
    self.firstName = f
    self.lastName = l
    self.age = -1
    self.jobsDone = []
    self.doingSomething = False

class Class:
  def __init__(self):
    self.name = ''
    self.room = 'none'
    self.teachers = []
    self.kids = []
    self.assignments = []

# determines if it will be general conference on the given date.
def isConference(aDate):
   if (aDate.month == 4 or aDate.month == 10): # if april or october
      if aDate.weekday() == 6: # if it's a sunday
         if aDate.day <= 7: #if it's the first one of the month
            return True
   return False

# def findIndexArray(num):
#    harray = []
#    if num % 2 == 0:
#       for i in range(0, num, 2):
#          harray.append(i + 1)
#          harray.append(i)
#    else:
#       for i in range(0, (num + 1), 2):
#          harray.append(i + 1)
#          harray.append(i)
#       del harray[num - 1]
#    return harray

# Returns all sundays in the given year
def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      if isConference(d) != True:
         yield d
      d += timedelta(days = 7)

# Parses the file of classes, students, and assignments.
def readFile(filename):
  listOfClasses = []
  file = open(filename, "r")
  indexOfClass = -1
  for line in file:
    mylistNoSpaces = ' '.join(line.split()) # gets rid of extra space
    mylist = mylistNoSpaces.split(" ")
    mylist = [x.rstrip('\n') for x in mylist]

    #Classes
    if mylist[0] == "Class:":
      listOfClasses.append(Class())
      indexOfClass += 1
      listOfClasses[indexOfClass].name = mylist[1]
    # Room
    elif mylist[0] == "Room:":
      listOfClasses[indexOfClass].room = mylist[1]
    # teacher
    elif mylist[0] == "Teacher:":
      somePerson = Person(mylist[1], mylist[2])
      listOfClasses[indexOfClass].teachers.append(somePerson)
    # teacher
    elif mylist[0] == "Kid:":
      somePerson = Person(mylist[1], mylist[2])
      listOfClasses[indexOfClass].kids.append(somePerson)
    # JOBS
    elif mylist[0] == "Assignments:":
      mylist = mylistNoSpaces.strip("Assignments:")
      mylist = mylist.split(",")
      mylist = [x.strip() for x in mylist]
      listOfClasses[indexOfClass].assignments = list(mylist)
    # print mylist
  return listOfClasses

# Displays the class
def displayClasses(myClasses):
  for c in myClasses:
    print("class name " + c.name)
    print("class location " + c.room)
    print("\nteachers: ")
    for teach in c.teachers:
      print(teach.firstName + " "),
    print("\n\nKids: ")
    for kid in c.kids:
      print(kid.firstName + " "),
    print("\n\njobs: ")
    for job in c.assignments:
      print(job + " "),
    print("\n")

# creates a text file
def writeFile(myClasses, year, filename):
  f = open(filename, "w")
  for aClass in myClasses:
    whichKid = 0
    for aDate in allsundays(year):
    # reset how busy people are
      for student in aClass.kids:
        student.doingSomething = False
      f.write(aClass.name + " -> " + aDate.strftime("%d-%b-%Y") + "\n")
      for assignment in aClass.assignments:
        madeAssignment = False
        for i in range(0, len(aClass.assignments)):
          if assignment in aClass.kids[whichKid].jobsDone:
            whichKid = (whichKid + 1) % len(aClass.kids)
            continue
          elif aClass.kids[whichKid].doingSomething:
            whichKid = (whichKid + 1) % len(aClass.kids)
            continue
          else:
            f.write("\t" + aClass.kids[whichKid].firstName + " " + aClass.kids[whichKid].lastName + " - " + assignment + "\n")
            aClass.kids[whichKid].jobsDone.append(assignment)
            aClass.kids[whichKid].doingSomething = True
            whichKid = (whichKid + 1) % len(aClass.kids)
            madeAssignment = True
            break
        if madeAssignment == False: # literally everyone has done the job...remove that item from every kid...
          for student in aClass.kids:
            if assignment in student.jobsDone:
              student.jobsDone.remove(assignment) 
          for student in aClass.kids:
            if aClass.kids[whichKid].doingSomething == False:
              aClass.kids[whichKid].doingSomething = True
              f.write("\t" + aClass.kids[whichKid].firstName +  " " + aClass.kids[whichKid].lastName + " - " + assignment + "\n")
              aClass.kids[whichKid].jobsDone.append(assignment)
              whichKid = (whichKid + 1) % len(aClass.kids)
              break
            else:
              whichKid = (whichKid + 1) % len(aClass.kids)
    f.write("\n")
  f.close()
################
# THIS IS MAIN #
################

readfileName = "putInNames.txt" #enter and erase primary names and assignemnt options
writeFileName = "primaryAssignments.txt" #this is what the program creates for the year. 
year = 2020


listOfClasses = readFile(readfileName)
writeFile(listOfClasses, year, writeFileName)

#Directions on how to you the program for Brittany!!! this is how you run the code. Hit control "B" and then go into the primary assigment tab.
#if you want to save you hit control "S". Do this after every change!
#If you want to search for a name hit control "F"
# Copy and paste needed info for each month for jr and sr. primary to a word document to print.





