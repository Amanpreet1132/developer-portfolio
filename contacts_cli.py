# contacts_cli.py
import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from the JSON file."""
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # Return an empty list if the file doesn't exist

def save_contacts(contacts):
    """Saves the contacts list to the JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    """Prompts user for contact info and adds it."""
    name = input("Enter contact name: ")
    email = input("Enter contact email: ")
    contacts.append({"name": name, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def list_contacts(contacts):
    """Displays all contacts."""
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}, Email: {contact['email']}")

def main():
    """Main function to run the contact book application."""
    contacts = load_contacts()
    while True:
        print("\nContact Book Menu:")
        print("1. Add a new contact")
        print("2. List all contacts")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            print("Exiting contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()