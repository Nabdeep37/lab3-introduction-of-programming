shoppingCart = {}
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("A. Add product to the cart.")
print("B. Search the product.")
print("C. Delete the product from the cart.")
print("D. Quit.")


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

def deleteProduct():
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
    print("you have done")
    choice = input("Enter your choice: ")

    if choice == 'A':
        addProduct()
    elif choice == 'B':
        searchProduct()
    elif choice == 'C':
        deleteProduct()
    elif choice == 'D':
        break
    else:
        print("Invalid choice")