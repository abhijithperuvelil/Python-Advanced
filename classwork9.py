# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
class Student:
    def __init__(self):
        self.rollnumber=int(input("Enter the Roll Number: "))
        self.name=input("Enter the Name: ")
        self.marks=int(input("Enter the Marks: "))
    def update(self):
        self.marks = int(input("Enter the New Marks: "))
        print("Marks Updated")
    def details(self):
        print("Roll Number is",self.rollnumber)
        print("Name is ", self.name)
        print("Mark is ", self.marks)
l=[]
while(1):
    print("Student MENU")
    print("Option 1 : Add Student ")
    print("Option 2 : Update Marks")
    print("Option 3 : Display All Student Details")
    print("Option 4 : Search Student")
    print("Option 5 : Delete Student")
    print("Option 6: Exit")
    ch=int(input("Enter the Choice: "))
    if ch==1:
        s=Student()
        l.append(s)
    elif ch==2:
        number=int(input("Enter the Roll Number: "))
        for i in l:
            if i.rollnumber==number:
                i.update()
                break
        else:
            print("Student Does Not Exit")
    elif ch==3:
        for i in l:
            i.details()
    elif ch==4:
        number = int(input("Enter the Roll Number: "))
        for i in l:
            if i.rollnumber == number:
                print("Student Found")
                break
        else:
            print("Student Does Not Exist")
    elif ch==5:
        number = int(input("Enter the Roll Number: "))
        for i in l:
            if i.rollnumber == number:
                l.remove(i)
                break
        else:
            print("Student Does not Exist")
    else:
        exit()





