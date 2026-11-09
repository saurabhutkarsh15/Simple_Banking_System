import json
print("===== Welcome To My Simple Banking System =====")

def create_account(account_info , next_accountnumber):
    name = input("Enter your name: ")
    deposit = float(input("Enter amount to be deposited for a new accont: "))

    if deposit <= 0:
        print("Amount to be deposited cannot be zero or negative.\n")
        return next_accountnumber

    account_info[next_accountnumber] = {
        "name" : name,
        "balance" : deposit
    }
    saved_accounts(account_info)
    print("Your Account is succesfully created.")
    print(f"Your Account Number is {next_accountnumber}")
    print(f"Your current balance is {deposit}\n")
    return next_accountnumber + 1

def deposit_money(account_info):
    account_number = int(input("Enter your account number: "))
    if account_number not in account_info:
        print("Account doesn't exist.\n")
        return
    
    amount = float(input("Enter the amount to be deposited: "))

    if amount <= 0:
        print("Deposit amount can't be negative or zero.\n")
    else:
        account_info[account_number]["balance"] += amount
        saved_accounts(account_info)
        print("Deposited Successfully!")
        print(f"Your currrent balance is {account_info[account_number]["balance"]}\n")

def withdraw_money(account_info):
    account_number = int(input("Enter your account number: "))
    if account_number not in account_info:
        print("Account doesn't exist.\n")
        return
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount <= 0:
        print("Amount to be withdrawn can't be negative or zero.\n")
        return

    current_bal = account_info[account_number]["balance"]
    if current_bal - amount < 500:
        print("Can't be withdrawn as minimum 500 should be maintained after withdrawal\n")
        return

    account_info[account_number]["balance"] -= amount
    saved_accounts(account_info)
    print("Withdrawal Successfull!")
    print(f"Your current balance is {account_info[account_number]["balance"]}\n")

def transfer_money(account_info):
    reciever_acc = int(input("Enter reciever acount number: "))
    sender_acc = int(input("Enter sender account number: "))
    if reciever_acc not in account_info or sender_acc not in account_info:
        print("Either bot or any one of the account doesn't exist.\n")
        return
    if sender_acc == reciever_acc:
        print("Money can't be transferred to the sane account.\n")
        return
    
    amount = float(input("Enter the amount to be transferred: "))

    if amount <= 0:
        print("Amount to be tranferred can't be negative or zero.\n")
        return

    sender_bal = account_info[sender_acc]["balance"]
    if sender_bal - amount < 500:
        print("Transfer rejected. Minimum balance of 500 should remain.\n")
        return

    account_info[sender_acc]["balance"] -= amount
    account_info[reciever_acc]["balance"] += amount
    saved_accounts(account_info)
    print("Transfer Successful!")
    print(f"Remaining of Sender's account is {account_info[sender_acc]["balance"]}\n")
    print(f"Remaining of Reciever's account is {account_info[reciever_acc]["balance"]}\n")

def check_balance(account_info):
    account = int(input("Enter your account number: "))

    if account not in account_info:
        print("Account doesn' exist.")
        return

    print("Account holder:", account_info[account]["name"])
    print("Current balance:", account_info[account]["balance"],"\n")

def saved_accounts(account_info):
    with open("bank.txt", "w") as file:
        json.dump(account_info , file , indent = 4)

def load_acc():
    try:
        with open("bank.txt", "r") as file:
            saved_data = json.load(file)
            account_info = {
                int(number) : details
                for number,details in saved_data.items()
            }
        return account_info

    except (FileNotFoundError, json.JSONDecodeError):
        return{} 

account_info = load_acc()
next_accountnumber = max(account_info.keys(), default= 1000) + 1

while True:
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")

    choice = int(input("Enter your choice(1 - 6): "))
    if choice == 1:
        print("You choose to create new account.")
        next_accountnumber = create_account(account_info , next_accountnumber)
    elif choice == 2:
        print("You choose deposit money.")
        deposit_money(account_info)
    elif choice == 3:
        print("You choose to withdraw money.")
        withdraw_money(account_info)
    elif choice == 4:
        print("You choose to transfer money.")
        transfer_money(account_info)
    elif choice == 5:
        print("You choose to check balance.")
        check_balance(account_info)
    elif choice == 6:
        print("Thank You for visiting us.\n")
        break
    else:
        print("Invalid choice. Pleae select from 1-6.\n")
