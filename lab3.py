shoppingCart = {}
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("1. Add product to the cart.")
print("2. Search the product.")
print("3. Delete the product from the cart.")
print("4. Quit.")


def addProduct():
    if len(shoppingCart) >= 5:
        print("Cart is full")
        return
    for i in range(2):
     item = input("Enter product name: ")
     brand = input("Enter brand: ")
     shoppingCart[item] = brand
    print("Product added successfully")

def searchProduct():
    item = input("Enter product name to search: ")
    if item in shoppingCart:
        print("Brand:", shoppingCart[item])
    else:
        print("No product exists with this name")

def delProduct():
    if len(shoppingCart) == 0:
        print("Cart is empty, no item is found")
        return
    
    item = input("Enter product name to delete: ")
    if item in shoppingCart:
        del shoppingCart[item]
        print("Product deleted successfully")
    else:
        print("No product exists with this name")

while True:

    choice = input("Enter your choice: ")

    if choice == '1':
        addProduct()
    elif choice == '2':
        searchProduct()
    elif choice == '3':
        delProduct()
    elif choice == '4':
        break
    else:
        print("Invalid choice")