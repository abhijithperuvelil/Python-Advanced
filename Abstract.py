# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("Enter the Length: "))
#         self.breadth=int(input("Enter the Breadth: "))
#     def get_area(self):
#         print("Area is ",self.length*self.breadth)
#     def get_perimeter(self):
#         print("Perimeter is",(self.length+self.breadth)*2)
# class Square(Shape):
#     def __init__(self):
#         self.side = int(input("Enter the Side: "))
#     def get_area(self):
#         print("Area is ",self.side*self.side)
#     def get_perimeter(self):
#         print("Perimeter is ", self.side *4)
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
# s=Square()
# s.get_area()
# s.get_perimeter()
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self):
        self.id = int(input("Enter the Id: "))
        self.name = input("Enter the Name: ")
        self.age = int(input("Enter the Age: "))
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = int(input("Enter the Salary: "))
    def calculate_salary(self):
        print("Salary is", self.salary)
class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hours = int(input("Enter the Working Hours: "))
        self.rate = int(input("Enter the Rate: "))
    def calculate_salary(self):
        print("Salary is", self.hours * self.rate)
e = FullTimeEmployee()
e.calculate_salary()
ep = PartTimeEmployee()
ep.calculate_salary()