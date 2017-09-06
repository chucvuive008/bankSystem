import random
class BankAccount:
    def __init__(seft):
        print("What is your name?")
        seft.name = input()
        print("How much do you want to deposit for your new account?")
        seft.balance = input()
        seft.accountNumber = random.randint(10000, 99999)
    
    def __init__(seft, n, ba):
        seft.name = n
        seft.balance = ba
        seft.accountNumber = random.randint(10000, 99999)

    def deposit(seft):
        print("How much do you want to deposit")
        amount = float(input())
        print("confirm. Did you want to deposit {}", amount)
        confirm = input()
        if confirm == "yes":
            seft.balance = seft.balance + amount
        else:
            print ("please wait a second for reset the deposit process")
            seft.deposit()

    def withDraw (seft):
        print("How much do you want to withdraw")
        amount = input()
        print("confirm. Did you want to withdraw {}", amount)
        confirm = input()
        if confirm == "yes":
            seft.balance = seft.balance + amount
        else:
            print ("please wait a second for reset the withdraw process")
            seft.withDraw()

    def printBalance(seft):
        print("This is your balance: {}",seft.balance)


account1 = BankAccount("Nghia", 200.9)
account2 = BankAccount("Thong", 2123.43)
List = [account1,account2]
for i in List:
    print(i.accountNumber)
print("Do You have account with us?(yes or no)")
fQuestion = input()
if fQuestion == "yes":
    print("please provide your account number and name")
    print("Account number:")
    checkAccountNumber = int(input())
    print("Your name:")
    checkName = input()
    for i in List:
        if i.name == checkName and i.accountNumber == checkAccountNumber:
            print("What can I have you today? (deposit, withdraw , or print balance")
            request = input()
            if request == "deposit":
                i.deposit()
            elif request == "withdraw":
                i.deposit()
            elif request == "print balance":
                i.printBalance()
        else:
            print("I didn't find any account with providing information")
else:
    print("Do you want to open a saving account with us?(yes or no)")
    openAccount = input()
    if openAccount == "yes":
        newAccount = BankAccount()
    else:
        print("Thank you for visiting our bank. Please come back in the future if you want to open an account with us")
