 # 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()
# class Movie:
#     def __init__(self):
#         self.movie_name=input("Enter the Movie Name: ")
#         self.year=int(input("Enter the Year: "))
#         self.language=input("Enter the language: ")
#         self.director=input("Enter the Name of the Director: ")
#         self.rating=int(input("Enter the Rating of the Movie: "))
#     def display_details(self):
#         print("Movie Name is ",self.movie_name)
#         print("Year is ",self.year)
#         print("Language of the Movie",self.language)
#         print("Director is ",self.director)
#         print("Rating of the Movie",self.rating)
#     def update_rating(self):
#         self.rating=int(input("Enter the New Rating: "))
#         print("New Rating is ",self.rating)
# m=Movie()
# m.display_details()
# m.update_rating()
#  2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
class Vehicle:
    def __init__(self):
        self.brand=input("Enter the Brand Name: ")
        self.model=input("Enter the Model: ")
        self.color=input("Enter the Color: ")
        self.year = input("Enter the Year: ")
    def display(self):
        print("Brand Name is ",self.brand,"Model is ",self.model,"Color is ",self.color,"Year is ",self.year)
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage=int(input("Enter the Mileage: "))
    def display(self):
        super().display()
        print("Mileage is ", self.mileage)
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc=int(input("Enter the CC: "))
    def display(self):
        super().display()
        print("CC is ", self.cc)
c=Car()
c.display()
b=Bike()
b.display()
