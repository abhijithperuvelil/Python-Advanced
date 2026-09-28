##### SINGLE LEVEL INHERITANCE


# class Parent:
#     def m1(self):
#         print("In class Parent m1")
#     def m2(self):
#         print("In class Parent m2")
# class Child(Parent):
#     def m3(self):
#         print("In class Parent m3")
# c=Child()
# c.m1()
# c.m2()
# c.m3()
## Method Overriding
# class Parent:
#     def m1(self):
#         print("In class Parent m1")
#     def m2(self):
#         print("In class Parent m2")
# class Child(Parent):
#     def m3(self):
#         print("In class Parent m3")
#     def m1(self):
#         print("In class Child m1")
# c=Child()
# c.m1()
# c.m2()
# c.m3()
### To call m1 from Parent and m1 from child
# class Parent:
#     def m1(self):
#         print("In class Parent m1")
#     def m2(self):
#         print("In class Parent m2")
# class Child(Parent):
#     def m3(self):
#         print("In class Parent m3")
#     def m1(self):
#         super().m1() # used to completely modify/extend the parent functionality
#         print("In class Child m1")
# c=Child()
# c.m1()
# c.m2()
# c.m3()
# class Person:
#     def __init__(self):
#         self.name=input("Enter the Name: ")
#         self.age=int(input("Enter the Age: "))
#     def show(self):
#         print("Name is ",self.name,"Age is ",self.age)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.marks = int(input("Enter the Marks: "))
#         self.rollno = int(input("Enter the Roll Number: : "))
#     def show(self):
#         super().show()
#         print("Mark is ",self.marks,"Roll Number is ",self.rollno)
#     def update(self):
#         self.marks=int(input("Enter the New Marks: "))
#         print("Updated Marks",self.marks)
# s=Student()
# s.show()
# s.update()
# class Category:
#     def __init__(self):
#         self.name=input("Enter the Category Name: ")
#     def show(self):
#         print("Category Name is",self.name)
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.name=input("Enter the Product Name: ")
#         self.price=int(input("Enter the Price: "))
#         self.quantity=int(input("Enter the Quantity: "))
#         self.total=self.price*self.quantity
#     def show(self):
#         super().show()
#         print("Total Price is ",self.total)
# p1=Product()
# p1.show()

# class Company:
#     def __init__(self):
#         self.company_name=input("Enter the Company Name: ")
#         self.location=input("Enter the Location: ")
#     def display(self):
#         print("Name of the Company is ",self.company_name)
#         print("Location of the Company is ",self.location)
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.id=int(input("Enter the Id: "))
#         self.name=input("Enter the Name: ")
#         self.salary=int(input("Enter the Salary: "))
#     def display(self):
#         super().display()
#         print("Id is ",self.id,"Name is ",self.name,"Salary is ",self.salary)
#     def update(self):
#         self.salary=self.salary*0.10+self.salary
#         print("Updated Salary is ",self.salary)
# e1=Employee()
# e1.display()
# e1.update()