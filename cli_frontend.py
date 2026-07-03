import requests

API_URL = "http://127.0.0.1:5000/inventory"

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
            response = requests.get(API_URL)
            items = response.json().get('inventory', [])
            if not items:
                print("No items found.")
            else:
                for item in items:
                    print(item)
                    
        if choice == "2":
            id = input("Enter item ID: ")
            response = requests.get(f"{API_URL}/{id}")
            if response.status_code == 200:
                item = response.json().get('item')
                print(item)
            else:
                print("Item not found.")
                
        if choice == "3":
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            response = requests.post(API_URL, json={"name": name, "price": float(price)})
            if response.status_code == 201:
                item = response.json().get('item')
                print(item)
            else:
                print("Item not created.")
                
        if choice == "4":
            id = input("Enter item ID: ")
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            response = requests.patch(f"{API_URL}/{id}", json={"name": name, "price": float(price)})
            if response.status_code == 200:
                item = response.json().get('item')
                print(item)
            else:
                print("Item not updated.")
                
        if choice == "5":
            id = input("Enter item ID: ")
            response = requests.delete(f"{API_URL}/{id}")
            if response.status_code == 200:
                print("deleted successfully")
            else:
                print("Item not deleted.")
                
        if choice == "6":
            break

if __name__ == '__main__':
    main()
