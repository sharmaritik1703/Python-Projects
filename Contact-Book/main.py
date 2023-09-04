__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

import json

print("Welcome to Contact Book")
print("You can store your contacts in our database.")
active = True

def show_contacts():
    source_file = open("contacts.json", mode="r")
    contents = json.load(source_file)
    for number in range(len(contents)):
        print(f"{contents[number]['name']} --> {contents[number]['number']}")

def add_contacts(name: str, contact: str):
    main_file = open("contacts.json", mode="r+")
    # Reads the content from file
    contents = json.load(main_file)
    data_template = {
            "name": name,
            "number": contact
    }
    # Adds data!
    contents.append(data_template)

    # Bring cursor to start!
    main_file.seek(0)

    # Adding into file!
    json.dump(contents, main_file, indent=4)

def search(contact_number: str):
    with open("contacts.json", mode="r") as my_file:
        data = json.load(my_file)
        for info in data:
            if info["number"] == contact_number:
                print(f"Person's Name: {info['name']}")

while active:
    print("""\nEnter one of the following operations to run the program:
    1 - Adding Contacts
    2 - Showing Contacts
    3 - Searching Information 
    0 - exit
    """)
    prompt = int(input("Enter the mode: "))
    if prompt == 1:
        recipient_name = input("Enter the name of recipient: ")
        contact_value = input("Enter recipient's contact number: ")
        add_contacts(recipient_name, contact_value)

    elif prompt == 2:
        print("\nThese are your saved contacts...")
        show_contacts()

    elif prompt == 3:
        search("8219985227")

    elif prompt == 0:
        active = False
