#
#====================================================================
#================================
# PROJECT NAME : SMART BANK SYSTEM
# DEVELOPPER : AYMAN KHAN
# LANGUAGE : PYTHON
#====================================================================
#================================

class Account:
    def __init__(self , account_number,holder_name,age,pin):
        self.account_number = account_number
        self.holder_name = holder_name
        self.age = age
        self.pin = pin
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self):
        amount = float(input("ENTER AMOUNT TO DEPOSIT:"))

        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"deposited: {amount}")
            print(f"\n {amount} MONEY DEPOSITD SUCCESSFULLU!")
            print(f"CURRENT BALANCE : {self.balance}")
        else:
            print("INVALID AMOUNT ! PLEASE ENTER A POSITIVE VALUE.")


    def withdraw(self): 
        amount = float(input("ENTER AMOUNT TO WITHDRAW:"))

        if amount <= 0:
            print("INVALID AMOUNT ! PLEASE ENTER A POSITIVE VALUE.")

        elif amount > self.balance:
            print("INSUFFICIENT BALANCE!")

        else:
            self.balance -= amount
            self.transaction_history .append(f"WITHDRAWN:-₹{amount}")
            print(f"\n {amount} MONEY WITHDRAWN SUCCESSFULLY!")
            print(f"CURRENT BALANCE : ₹ {self.balance}")


    def show_balance(self):
        print("\n======ACCOUNT DETAILS======")
        print(f"ACCOUNT NUMBER : {self.account_number}")
        print(f"ACCOUNT HOLDER : {self.holder_name}")
        print(f"AGE : {self.age}")
        print(f"CURRENT BALANCE : ₹ {self.balance}")


    def view_transactions(self):
        print("\n======TRANSACTION HISTORY======")

        if len(self.transaction_history) == 0:
            print("NO TRANSACTIONS FOUND!")

        else:
            for transaction in self.transaction_history:
                print(transaction)            



class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("ENTER YOUR ACCOUNT NUMBER:")
        holder_name = input("ENTER ACCOUNT HOLDER NAME:")
        age = int(input("ENTER YOUR AGE:"))
        pin = input("SET 4-DIGIT PIN:")

        account = Account(account_number , holder_name , age , pin)
        self.accounts[account_number] = account

        print("\n ACCOUNT CREATED SUCCESSFULLY!")


    def login(self):
        account_number = input("ENTER YOUR ACCOUNT NUMBER:")
        pin = input("ENTER YOUR PIN:")

        account = self.accounts.get(account_number)
        if account and account.pin == pin:
                print("\n LOGIN SUCCESSFUL!")
                return account
        
        print("\n INVALID ACCOUNT NUMBER OR PIN!")
        return None

    def find_account(self,account_number):
     return self.accounts.get(account_number)
    

    def transfer_funds(self,sender):
        receiver_account_number = input("ENTER RECEIVER ACCOUNT NUMBER:")
        receiver = self.find_account(receiver_account_number)

        if receiver is None:
            print("RECEIVER ACCOUNT NOT FOUND!")
            return
        amount = float(input("ENTER AMOUNT TO TRANSFER :₹"))

        if amount <= 0:
            print("INVALID AMOUNT!")
            return

        if amount > sender.balance:
            print("INSUFFICIENT BALANCE!")
            return
        sender.balance -= amount
        receiver.balance += amount
        sender.transaction_history.append(f"Transferred ₹{amount}to {receiver.account_number}")
        receiver.transaction_history.append(f"Received ₹{amount} from {sender.account_number}")
        print(f"\n₹{amount} TRANSFERRED SUCCESSFULLY!")
        print(f"YOUR CURRENT BALANCE : ₹ {sender.balance}")

bank = Bank()
current_account = None            

    

while True:

    print("\n================SMART BANK ====================")
    print("1 . CREATE ACCOUNT")
    print("2 . LOGIN")
    print("3 . DEPOSIT MONEY")
    print("4 . WITHDRAW MONEY")
    print("5 . CHECK BALANCE")
    print("6 . TRANSFER FUNDS")
    print("7 . TRANSACTION HISTORY")
    print("8 . EXIT")

    choice = input("ENTER YOUR CHOICE :").strip()

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        current_account = bank.login()

    elif choice == "3":
        if current_account:
            current_account.deposit()
        else:
            print("PLEASE LOGIN FIRST!")


    elif choice == "4":
        if current_account:
            current_account.withdraw()
        else:
            print("PLEASE LOGIN FIRST!")


    elif choice == "5":
        print(current_account)
        if current_account:
            current_account.show_balance()
        else:
            print("PLEASE LOGIN FIRST!")


    elif choice == "6":
        if current_account:
            bank.transfer_funds(current_account)
        else:
            print("PLEASE LOGIN FIRST!")


    elif choice == "7":
        if current_account:
            current_account.view_transactions()
        else:
            print("PLEASE LOGIN FIRST!")

    elif choice == "8":
        print("\n THANK YOU FOR USING SMART BANK!!")
        print("HAVE A SAFE AND SECURE DAY !")
        break

    else:
        print("INVALID CHOICE PLEASE TRY AGAIN.")
