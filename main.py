# Create Contacts List
# based on https://pythonalgos.com/super-simple-python-contacts-list/

import json

def save_contact(filename: str):
    # Get data
    name = input("Contact name? ")
    email = input("Contact email? ")
    phone = input("Contact phone? ")
    relationship = input("Contact relationship? ")
    # Link responses to a format to add to json
    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "relationship": relationship
    }
    # Add contact to json file
    with open(filename, "a") as f:
        json.dump(contact, f)

if __name__ == '__main__':
    # Introduction
    print("This program saves a Contact in your Contacts List")
    # Declare file location
    filename = 'contacts.json'
    # Run function to get new contact data and save it to json file
    save_contact(filename)