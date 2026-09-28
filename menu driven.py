# class Account:
#     def __init__(self):
#         self.acctnumber=int(input("Enter the Number: "))
#         self.name=input("Enter the Name: ")
#         self.balance=int(input("Enter the Balance: "))
#     def withdraw(self):
#         amount=int(input("Enter the Amount: "))
#         if amount>self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             self.showbalance()
#     def showbalance(self):
#         print("Total Balance is ",self.balance)
#
#     def deposit(self):
#         amount = int(input("Enter the Amount: "))
#         self.balance += amount
#         self.showbalance()
# l=[]
# while(1):
#     print("BANKING MENU")
#     print("Option 1 : Create A New Account")
#     print("Option 2 : Withdraw")
#     print("Option 3 : Deposit")
#     print("Option 4 : Show Balance")
#     print("Option 5 : Exit")
#     ch=int(input("Enter the Choice: "))
#
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print("Account Created ")
#         # print(l)
#     elif ch == 2:
#         number = int(input("Enter the Account Number: "))
#         for i in l:
#             if i.acctnumber == number:
#                 i.withdraw()
#                 break
#         else:
#             print("Account not Exist")
#     elif ch == 3:
#         number = int(input("Enter the Account Number: "))
#         for i in l:
#             if i.acctnumber == number:
#                 i.deposit()
#                 break
#             else:
#                 print("Account not Exist")
#     elif ch==4:
#         number = int(input("Enter the Account Number: "))
#         for i in l:
#             if i.acctnumber == number:
#                 i.showbalance()
#                 break
#             else:
#                 print("Account not Exist")
#     elif ch == 5:
#         exit()
# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
# class Student:
#     def __init__(self):
#         self.rollnumber=int(input("Enter the Roll Number: "))
#         self.name=input("Enter the Name: ")
#         self.marks=int(input("Enter the Marks: "))
#     def update(self):
#         self.marks = int(input("Enter the New Marks: "))
#         print("Marks Updated")
#     def details(self):
#         print("Roll Number is",self.rollnumber)
#         print("Name is ", self.name)
#         print("Mark is ", self.marks)
# l=[]
# while(1):
#     print("Student MENU")
#     print("Option 1 : Add Student ")
#     print("Option 2 : Update Marks")
#     print("Option 3 : Display All Student Details")
#     print("Option 4 : Search Student")
#     print("Option 5 : Delete Student")
#     print("Option 6: Exit")
#     ch=int(input("Enter the Choice: "))
#     if ch==1:
#         s=Student()
#         l.append(s)
#     elif ch==2:
#         number=int(input("Enter the Roll Number: "))
#         for i in l:
#             if i.rollnumber==number:
#                 i.update()
#                 break
#         else:
#             print("Student Does Not Exit")
#     elif ch==3:
#         for i in l:
#             if i.details==l:
#                 i.details()
#     elif ch==4:
#         number = int(input("Enter the Roll Number: "))
#         for i in l:
#             if i.rollnumber == number:
#                 print("Student Found")
#                 break
#         else:
#             print("Student Does Not Exist")
#     elif ch==5:
#         number = int(input("Enter the Roll Number: "))
#         for i in l:
#             if i.rollnumber == number:
#                 l.remove(i)
#                 break
#         else:
#             print("Student Does not Exist")
#     else:
#         exit()





