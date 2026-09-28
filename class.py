# class PERSON:
#     def __init__(self ,n,a):
#         self.name=n
#         self.age=a
#     def show(self):
#         print(self.name,self.age)
# p1=PERSON("arun",23)
# p1.show()
# p2=PERSON("amal",25)
# p2.show()
# DYNAIMIC
# class PERSON:
#     def __init__(self):
#         self.name=input("Enter the Name: ")
#         self.age=int(input("Enter the Age"))
#     def show(self):
#         print(self.name,self.age)
# p1=PERSON()
# p1.show()
# p2=PERSON()
# p2.show()
# class EMPLOYEE:
#     def __init__(self):
#             self.id = int(input("Enter Employee ID: "))
#             self.name = input("Enter Name: ")
#             self.age = int(input("Enter Age: "))
#             self.salary = int(input("Enter Salary: "))
#             self.designation = input("Enter Designation: ")
#     def showsalary(self):
#         print("Salary ",self.salary)
#     def show(self):
#         print(self.name,self.id,self.age)
# e1=EMPLOYEE()
# e1.showsalary()
# e1.show()
# Define a class of a student of attribute roll number , name , mark1 , mark2, mark3 and method display() to display roll number and
# total mark of  a student
# create a student of objet and call the methods
# class STUDENT:
#     def __init__(self):
#         self.rollnumber=int(input("Enter the Roll Number: "))
#         self.name=input("Enter the Name: ")
#         self.mark1 = int(input("Enter the Mark 1: "))
#         self.mark2 = int(input("Enter the Mark 2: "))
#         self.mark3 = int(input("Enter the Mark 3: "))
#         self.total=self.mark1+self.mark2+self.mark3
#     def display(self):
#         print("Roll Number is",self.rollnumber,"Total Mark is ",self.total)
# s=STUDENT()
# s.display()
#create a class named book with attributes  title,author ,price,page,language and methods
# get title ,get author get price
#set title set author set price
# class BOOK:
#     def __init__(self):
#         self.title = input("Enter the Title: ")
#         self.author = input("Enter the Name of the Author: ")
#         self.price = int(input("Enter the Price: "))
#         self.page = int(input("Enter the Number of Pages: "))
#         self.language = input("Enter the Language: ")
#     def gettitle(self):
#         print("Title of the BOOK is", self.title)
#     def getauthor(self):
#         print("Author of the BOOK is", self.author)
#     def getprice(self):
#         print("Price of the BOOK is", self.price)
#     def settitle(self):
#         self.title = input("Enter the New Title: ")
#         self.gettitle()
#     def setauthor(self):
#         self.author = input("Enter the New Author: ")
#         self.getauthor()
#     def setprice(self):
#         self.price = int(input("Enter the New Price: "))
#         self.getprice()
# b1 = BOOK()
# b1.gettitle()
# b1.getauthor()
# b1.getprice()
# b1.settitle()
# b1.setauthor()
# b1.setprice()
#Create a class name accountant with attributes acc name,accnumber ,acc balance and methods withdraw deposit and showbalance
# Create a class named ACCOUNT with attributes
# name, account number, balance
# Methods: withdraw, deposit, showbalance
class ACCOUNT:
    def __init__(self):
        self.name = input("Enter the Name: ")
        self.accnumber = int(input("Enter the Account Number: "))
        self.balance = int(input("Enter the Balance: "))
    def acctname(self):
        print("name is ",self.name)
    def withdraw(self):
        amount = int(input("Enter the Amount to Withdraw: "))
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
            self.showbalance()
    def deposit(self):
        amount = int(input("Enter the Amount to Deposit: "))
        self.balance = self.balance + amount
    def showbalance(self):
        print("Total Balance is", self.balance)
a1 = ACCOUNT()
a2=ACCOUNT()
# a1.withdraw()
# a1.deposit()
# a1.showbalance()
l=[a1,a2]
for i in l:
    print(i.acctname)
    i.showbalance()