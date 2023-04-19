phonebook = {}

def add_phone_number():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phonebook[name] = phone
    print(f"Added {name} with phone number {phone} to phonebook.")

def remove_phone_number():
    name = input("Enter name to remove: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Removed {name} from phonebook.")
    else:
        print(f"{name} not found in phonebook.")

def lookup_phone_number():
    name = input("Enter name to look up: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook.")

print("Phonebook\n")

while True:
    print("Choose an option:")
    print("1. Add phone number")
    print("2. Remove phone number")
    print("3. Look up phone number")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == '1':
        add_phone_number()
    elif choice == '2':
        remove_phone_number()
    elif choice == '3':
        lookup_phone_number()
    else:
        print("Invalid input.")
