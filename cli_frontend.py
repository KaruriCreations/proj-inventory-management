import requests
from app import get_all_items, get_item, create_item, update_item, delete_item

def show_menu():
    print("\n=== Inventory Management System ===")
    print("1. Show all items")
    print("2. Show an item")
    print("3. Create an item")
    print("4. Update an item")
    print("5. Delete an item")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose a number between 1 and 6: ")
        if choice == "1":
            items = get_all_items()
            if not items:
                print("No items found.")
            else:
                for item in items:
                    print(item)
        if choice == "2":
            id = input("Enter item ID: ")
            item = get_item(id)
            if item:
                print(item)
            else:
                print("Item not found.")
        if choice == "3":
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            item = create_item(name, price)
            if item:
                print(item)
            else:
                print("Item not created.")
        if choice == "4":
            id = input("Enter item ID: ")
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            item = update_item(id, name, price)
            if item:
                print(item)
            else:
                print("Item not updated.")
        if choice == "5":
            id = input("Enter item ID: ")
            item = delete_item(id)
            if item:
                print(f"{item} has been deleted successfully")
            else:
                print("Item not deleted.")
        if choice == "6":
            break

        

        




