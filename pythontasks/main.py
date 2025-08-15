accounts=[
    {
        "name": "furkan",
        "account_number": 1001,
        "balance": 500.0
    },
    {
        "name": "shahidbhat",
        "account_number": 1003,
        "balance": 900.0
    },
    {
        "name": "munazah",
        "account_number": 1004,
        "balance": 2000.0
    }
]

def create_account():
    accounts=load_account()
    try:
        name=input("Enter the Name : ")
        balance=float(input("Enter the balance : "))
    except ValueError:
        print("Invalid input")
        return
    try:
        if accounts:
            account_number=accounts[-1]["account_number"]+1
        else:
            account_number=1001
        new_account={
            "name":name,
            "account_number":account_number,
            "balance":balance
        }
        accounts.append(new_account)
        save_accounts(accounts)
        print(f"✅ Account created successfully! Account Number: {account_number}")
    except Exception as e:
        print(f"Error: {e}")
        return
