#Ask the User to Enter a Number if the number is less than or equal to 0 raise a value error
# try:
#     n=int(input("Enter the Number: "))
#     if n<=0:
#         raise ValueError("Number Must Be Positive")
# except:
#     print("Number is Positive")
#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
# class InvalidPasswordError(Exception):
#     pass
# try:
#     p=input("Enter the Password: ")
#     if len(p)<=8 or len(p)>8:
#         raise InvalidPasswordError("Password Should Have 8 characters ")
#     else:
#      print(p)
# except InvalidPasswordError as e:
#     print(e)
#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
# class InsuffientBalanceError(Exception):
#     pass
# while(1):
#     try:
#         balance=int(input("Enter the Balance: "))
#         amount=int(input("Enter the Amount: "))
#         if amount>balance:
#             raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
#         else:
#             print("Transaction Completed Balance Amount is ",balance-amount)
#     except InsuffientBalanceError as e:
#         print(e)
# Ask the user for username and password.
#
# Rules:
#
# Username must not be empty.
# Password must contain at least 8 characters.
# Password must contain at least one digit.
class InvalidUsername(Exception):
    pass
class InvalidPasswordError(Exception):
    pass
try:
    username=input("Enter the Username: ")
    password=input("Enter the Password: ")
    if username=="":
        raise InvalidUsername("Username must not be empty.")
    if len(password)<8:
        raise InvalidPasswordError("Password Contains 8 digits")
    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError("Password Should Contain atleaset 1 digit")
except InvalidUsername as e:
        print(e)
except InvalidPasswordError as d:
            print(d)
else:
    print("Account Created")