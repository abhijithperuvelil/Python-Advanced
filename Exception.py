# while(1):
#     try:
#         n1=int(input("Enter the Number: "))
#         n2=int(input("Enter the Number: "))
#         s=n1//n2
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Character")
#     except:
#         print("Value Error")
#
#     else:
#         print("Result",s)
#     finally:
#         print("Done")
# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
import math
# while(1):
#     try:
#         n=int(input("Enter the Number: "))
#         fact = math.factorial(n)
#     except ValueError:
#         print("Value Error")
#     else:
#         print("Factorial",fact)
#         break
# def facto():
#         try:
#             n=int(input("Enter the Number: "))
#             fact = math.factorial(n)
#         except ValueError as e:
#             print(e)
#             facto() # Recursion Function a function that calls itself
#         else:
#             print("Factorial",fact)
# facto()

# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# while True:
#     try:
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
#         choice = int(input("Enter the Choice: "))
#         if choice in [1,2,3,4]:
#             n1 = int(input("Enter the Number: "))
#             n2 = int(input("Enter the Number: "))
#             s=n1+n2
#             r=n1-n2
#             d=n1*n2
#             m=n1/n2
#
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Inputs")
#     except:
#         print("Error:", )
#     else:
#         if choice == 1:
#             print("Result is", s)
#         elif choice == 2:
#             print("Result is", r)
#         elif choice == 3:
#             print("Result is", d)
#         elif choice == 4:
#             print("Result is", m)
#         else:
#          exit()


# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     s=input("Enter the File Name: ")
#     f=open(s,"r")
#     s=f.read()
# except:
#     print("file Does not Exist")
# else:
#     print(s)
#     f.close()




#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# try:
#     d={"name":"arun","age":23,"place":"ekm"}
#     key=input("Enter the Key: ")
#     print(d[key])
# except:
#     print("Invalid Key")
# class MyException(Exception):
#     pass
# try:
#         n=int(input("Enter the Age: "))
#         if n<18:
#             raise MyException("Not Eligible For Voting")
#         else:
#             print("Eligible For Voting")
# except MyException as e:
#         print(e)