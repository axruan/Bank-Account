import random as r

class bank:

    def __init__(self, pin, name, num, balance):
        self.p = pin
        self.name = name
        self.num = num
        self.b = balance

    def deposit(deposit, amount):
        deposit.a = amount

choice = input("Hello, welcome to Darth Bank! Press ENTER to continue.\n")
choice = input("Would you like to open an account? (Y/N)\n")
if input == "Y" or "y":
    name = input("What is your name? ")
    pin = input("Hello, " + str(name) + "! Choose a 4 digit pin: ")
    account = bank(pin, name, r.randint(10000000, 99999999), 0)
    choice = input("Account '" + str(account.name) + "' created with pin " + str(account.p) + ". Press any key to continue.")
    choice = input("Your account number is " + str(account.num) + ". Press any key to continue.")
    while True:
        choice = input("What would you like to do?\n   1) Check account balance\n   2) Make a deposit\n   3) Make a withdrawal\n\n")
        if choice == "1":
            print("Your account balance is: " + str(account.b))
