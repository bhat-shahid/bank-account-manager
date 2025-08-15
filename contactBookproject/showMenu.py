import json
import os

FILENAME = "contacts.json"

# Load contacts from file (or empty list if none)
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # File exists but is empty or broken
    return []  # No file exists yet

# Save contacts to file
def save_contacts():
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Start program with saved contacts
contacts = load_contacts()

def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()  # Save immediately after adding
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    print(f"{'Name':<20} {'Phone':<15} {'Email'}")
    print("-" * 50)

    for contact in contacts:
        print(f"{contact['name']:<20} {contact['phone']:<15} {contact['email']}")

def search_contact():
    if not contacts:
        print("No contacts found.")
        return

    search_name = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
            break

    if not found:
        print(f"No contact found with name '{search_name}'.")

def delete_contact():
    if not contacts:
        print("No contacts found.")
        return

    delete_name = input("Enter name to delete: ").lower()
    found = False

    for contact in contacts:
        if contact["name"].lower() == delete_name:
            contacts.remove(contact)
            save_contacts()  # Save after deleting
            print(f"Contact '{contact['name']}' deleted successfully!")
            found = True
            break

    if not found:
        print(f"No contact found with name '{delete_name}'.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
  
  