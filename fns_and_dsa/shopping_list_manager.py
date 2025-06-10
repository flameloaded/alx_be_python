def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the item you want to add.")
            shopping_list.append(add_item)
            print("Item added")
        elif choice == '2':
            remove_item = input("Enter the item you want to remove,")
            if len(shopping_list) == 0:
                print("empty stock")
            elif remove_item not in shopping_list:
                print("input not found")
            else:
                shopping_list.remove(remove_item)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            break
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()