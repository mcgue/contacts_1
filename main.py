# Create Contacts List
# based on https://pythonalgos.com/super-simple-python-contacts-list/

import json

def save_contact(contact: dict, filename: str):
    with open(filename, "a") as f:
        json.dump(contact, f)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("This program saves a Contact in your Contacts List")
    name = input("Contact name? ")
    email = input("Contact email? ")
    phone = input("Contact phone? ")
    relationship = input("Contact relationship? ")

    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "relationship": relationship
    }

    save_contact(contact, "contacts.json")

    # Print contacts
    # Opening JSON file
    f = open('contacts.json')

    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list to print
    #for i in data['emp_details']:
        #print(i)

    # Closing file
    #f.close()
