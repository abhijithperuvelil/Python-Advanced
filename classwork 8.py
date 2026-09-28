# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
class Circle:
    def __init__(self):
        self.radius = int(input("Enter the Radius: "))
    def getarea(self):
        print("Area is", self.radius * self.radius * 3.14)
    def getperimeter(self):
        print("Perimeter is", self.radius * 2 * 3.14)
c = Circle()
c.getarea()
c.getperimeter()
# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
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