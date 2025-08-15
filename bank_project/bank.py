import json
import os

# File path for accounts.json (stored in the same folder as script)
FILE_PATH = os.path.join(os.path.dirname(__file__), "accounts.json")

def save_accounts(accounts):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=4)
    print("✅ Accounts saved successfully.")

def load_accounts():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def create_account(accounts):
    name = input("Enter account holder's name: ").strip()
    account_number = input("Enter account number: ").strip()

    # Check for duplicate account number
    if any(acc["account_number"] == account_number for acc in accounts):
        print("⚠️ Account number already exists!")
        return

    try:
        balance = float(input("Enter initial deposit amount: "))
        if balance < 0:
            print("⚠️ Initial deposit cannot be negative.")
            return
    except ValueError:
        print("⚠️ Invalid amount.")
        return

    accounts.append({"name": name, "account_number": account_number, "balance": balance})
    save_accounts(accounts)
    print(f"✅ Account for {name} created successfully!")

def deposit(accounts):
    acc_num = input("Enter account number: ").strip()
    for acc in accounts:
        if acc["account_number"] == acc_num:
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("⚠️ Deposit amount must be greater than zero.")
                    return
                acc["balance"] += amount
                save_accounts(accounts)
                print(f"💰 Deposited {amount:.2f} to {acc['name']}'s account.")
                return
            except ValueError:
                print("⚠️ Invalid amount.")
                return
    print("⚠️ Account not found.")

def withdraw(accounts):
    acc_num = input("Enter account number: ").strip()
    for acc in accounts:
        if acc["account_number"] == acc_num:
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("⚠️ Withdrawal amount must be greater than zero.")
                    return
                if amount > acc["balance"]:
                    print("⚠️ Insufficient balance.")
                    return
                acc["balance"] -= amount
                save_accounts(accounts)
                print(f"🏧 Withdrawn {amount:.2f} from {acc['name']}'s account.")
                return
            except ValueError:
                print("⚠️ Invalid amount.")
                return
    print("⚠️ Account not found.")

def transfer(accounts):
    sender_acc = input("Enter sender's account number: ").strip()
    receiver_acc = input("Enter receiver's account number: ").strip()

    sender = next((acc for acc in accounts if acc["account_number"] == sender_acc), None)
    receiver = next((acc for acc in accounts if acc["account_number"] == receiver_acc), None)

    if not sender or not receiver:
        print("⚠️ One or both account numbers not found.")
        return

    try:
        amount = float(input("Enter transfer amount: "))
        if amount <= 0:
            print("⚠️ Transfer amount must be greater than zero.")
            return
        if amount > sender["balance"]:
            print("⚠️ Sender has insufficient funds.")
            return
        sender["balance"] -= amount
        receiver["balance"] += amount
        save_accounts(accounts)
        print(f"🔄 Transferred {amount:.2f} from {sender['name']} to {receiver['name']}.")
    except ValueError:
        print("⚠️ Invalid amount.")

def remove_account(accounts):
    acc_num = input("Enter account number to remove: ").strip()
    for acc in accounts:
        if acc["account_number"] == acc_num:
            accounts.remove(acc)
            save_accounts(accounts)
            print(f"🗑️ Account {acc['name']} removed successfully.")
            return
    print("⚠️ Account not found.")

def display_accounts(accounts):
    if not accounts:
        print("⚠️ No accounts to display.")
        return
    print("\n📋 All Accounts:")
    print(f"{'Name':<15} {'Account Number':<20} {'Balance':<10}")
    print("-" * 45)
    for acc in accounts:
        print(f"{acc['name']:<15} {acc['account_number']:<20} {acc['balance']:.2f}")

def main():
    accounts = load_accounts()
    while True:
        print("\n🏦 Bank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Funds")
        print("5. Remove Account")
        print("6. Display All Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            transfer(accounts)
        elif choice == "5":
            remove_account(accounts)
        elif choice == "6":
            display_accounts(accounts)
        elif choice == "7":
            print("👋 Thank you for using the system!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
