def display_menu():
    print('''Welcome to Contact Book!
          1. Add Contact
          2. View Contacts
          3. Search Contact
          4. Update Contact
          5. Delete Contact
          6. Exit''')

def add_contact(contacts):
    name = input("Enter the name: ").lower()
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    contacts.append([name, phone, email, address])
    print("Contact added successfully!")

def view_contacts(contacts):
    for index, contact in enumerate(contacts):
        name, phone, email, address = contact
        print(f"{index+1}. Name: {name}, Phone: {phone}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact]
    if found_contacts:
        for contact in found_contacts:
            name, phone, email, address = contact
            print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")
    else:
        print("No contacts found!")

def update_contact(contacts):
    name_to_update = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if name_to_update in contact:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact[1] = phone
            contact[2] = email
            contact[3] = address
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if name_to_delete in contact:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found!")


contacts = []
while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        update_contact(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        break
    else:
        print("Invalid option! \n Please try again!")

