# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:21:03 2020

@author: vinod
"""



##### Hash Table implementation to store student records#####
##### Contributions: Anju Thomas , Ansi Sharma , Vinod  #####

# sturec1 one instance of class studentRecord
#

class studentRecord:
    def __init__(self, studentID, cgpa):
        self.studentID=studentID
        self.cgpa=cgpa
        
class departmentRecord:   
    def __init__(self, name) :
        self.departmentName=name
        #TODO Store students in sorted list 
        self.StudentList=list() 
        self.maxCGPA=0
        self.avgCGPA=0
        self.numStudents=0
    def addStudent(self, studentID, cgpa):
        student=studentRecord(studentId, cgpa)
        if(cgpa>self.maxCGPA):
            self.maxCGPA=cgpa
       
        self.avgCGPA=((self.avgCGPA*self.numStudents)+cgpa)/(self.numStudents+1)
        self.numStudents+=1
        self.StudentList.append(student)


    

class academicYear:
    def __init__ (self, year):
       self.year=year
       self.department=list()
       self.department.insert(0, departmentRecord("CSE"))
       self.department.insert(1, departmentRecord("ECE"))
       self.department.insert(2, departmentRecord("MEC"))
       self.department.insert(3, departmentRecord("ARC"))
       
    def deptoID(id) :
        if id == "CSE":
            return 0
        if id == "ECE":
            return 1
        if id == "MEC":
            return 2
        if id == "ARC":
            return 3
      
class studentHashRecords:
    def __init__(self,n):
        self.nBucket=n
        
    def initializeHash(self):
        for i in range(self.nBucket):
            self.hashbucket(i,list())
            
    # strips the year from studentID     
    def studentHash(studentID):
        # the studentID[0:4] represents the year in student ID
        return (int(studentID[0:4]) % 6)
    
    def searchoraddRecord(year, recordList):
        for record in recordList:
            if record.year==year:
                return record
        
        record=academicYear(year)
        recordList.append(record)
        return record
        
        
            
    #def __del__(self):
        print("Destroying all Hash records")
        
    def insertStudent(self, studentID, cgpa):
        #TODO
            hashVal=studentHashRecords.studentHash(studentID)

            record=studentHashRecords.searchoraddRecord(int(studentID[0:4]),self.hashbucket[hashVal])
            # student[4:7] represents the branch in student ID
            departmentRecord=record.department[record.deptoID([studentID[4:7]])]
            departmentRecord.addStudent(studentID,cgpa)



"""Group 74 - DSAD Assignment - PS18, Hash table implementation assignment"""



def initializeHash(self):
  """This function creates an empty hash table and points to null """
  pass



def insertStudentRec(StudentHashRecords, studentId, CGPA):
  """
  This function inserts the student id and corresponding CPGA into the 
  hash table. 
  The inputs need to be read from a file inputPS18.txt which contains the 
  student ID and overall graduating CGPA 
  (decimal value with a maximum of 5.0 points). 
  The file read can happen outside the function and only the
  information in every individual row needs to be passed to the function.
  """
  pass

def hallOfFame(StudentHashRecords): 
  """
  This function prints the list of all students who have
  graduated and topped their department in their year of graduation 
  (Only students who graduated should be considered. 
  Calculate the applicable year range accordingly). 
  The trigger can be read from the file promptsPS18.txt. 
  The input can be identified with the tag --> hallOfFame:
  """
  pass


def newCourseList(StudentHashRecords, CGPAFrom, CPGATo): 
  """
  This function prints the
  list of all students who have a CGPA within the given range and have 
  graduated in the last 5 years (Only students who graduated should be 
  considered. Calculate the applicable year range accordingly). 
  The input CGPAs can be read from the file promptsPS18.txt. The input
  can be identified with the tag mentioned below -
  courseOffer: 3.5 : 4.0
  """
  pass


def depAvg(StudentHashRecords): 
  """
  This function prints the list of all departments followed
  by the maximum CGPA and average CGPA of all students in that department. 
  The output should be captured in outputPS18.txt following format
  Output format:
  ---------- department CGPA ----------
  CSE: max: 3.5, avg: 3.4
  MEC: max: 3.5, avg: 3.4
  ECE: max: 3.5, avg: 3.4
  ARC: max: 3.5, avg: 3.4
  -------------------------------------
  """
  pass

def destroyHash(StudentHashRecords): 
  """
  This function destroys all the entries inside hash
  table. This is a clean-up code.
  """
  pass

def helperFunction():
  """
  Custom function for error checking
  """
  pass

#f=open('/content/drive/MyDrive/DSAD/inputPS18.txt','r')
#print(insertStudentRec.__doc__)

#change file path when in colab.
#the input file should be in same folder as .py file when running in IDE
filein=open("inputPS18.txt",'r')
Lines=filein.readlines()
l=[]
rec=[]# empty list initialized for storing student records read from inputPS18.txt
for x in Lines:
    l.append((x.split(" / ")[0],x.split(" / ")[1].strip()))
for j in range(len(l)):
    rec.append(studentRecord(l[j][0],float(l[j][1])))
filein.close()


print(rec[5].studentID,rec[5].cgpa)

"""

var1=studentHashRecords(6)
var2=studentHashRecords.studentHash("2014MEC1443")
## below line gives the following attribute error
var1.insertStudent(rec[5].studentID, rec[5].cgpa)

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-140-86167ff2ede0> in <module>
----> 1 var1.insertStudent(rec[5].studentID, rec[5].cgpa)

<ipython-input-136-6a29aa39d624> in insertStudent(self, studentID, cgpa)
     81 
     82             record=studentHashRecords.searchoraddRecord(int(studentID[0:4]),
---> 83                                          self.hashbucket[hashVal])
     84             # student[4:7] represents the branch in student ID
     85             departmentRecord=record.department[record.deptoID([studentID[4:7]])]

AttributeError: 'studentHashRecords' object has no attribute 'hashbucket'

"""
## continue code from below