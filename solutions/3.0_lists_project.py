grocery_list = []

print("Welcome to Grocery List!")
while True:
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Check if an item is on the list")
    print("4. Display the current list")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(item, "has been added to the list.")

    elif choice == 2:
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(item, "has been removed from the list.")
        else:
            print("Error: {} is not on the list.".format(item))

    elif choice == 3:
        item = input("Enter the item to check: ")
        if item in grocery_list:
            print(item, "is on the list.")
        else:
            print(item, "is not on the list.")

    elif choice == 4:
        print("Current list:", grocery_list)

    elif choice == 5:
        break

    else:
        print("Error: Invalid choice")
