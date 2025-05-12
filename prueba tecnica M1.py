# initial inventory
stock = [
    {"name": "Pintura", "price": 30, "amount": 5},
    {"name": "Pincel", "price": 10, "amount": 10},
    {"name": "Martillo", "price": 15, "amount": 3},
    {"name": "Taladro", "price": 50, "amount": 10},
    {"name": "Broca", "price": 5, "amount": 10}
]

# Function to display the options menu
def show_menu():
    print("---MAIN MENU INVENTORY MANAGEMENT---")
    print("1. Add product") # Option for adding an item
    print("2. Search product") # Option to search for products
    print("3. Update product") # Option to update a product
    print("4. Delete product") # Option to Delete a product
    print("5. Calculate the value of inventory") # Option to calculate the value of the stock
    print("6. exit") # Option to end the program

# Function to display all products available in the inventory.
def show_available_products(stock):
    print("\n---List of products available in inventory---")
    for product in stock:
        print(f"- {product['name']}") # Print the name of each product in the inventory

# Function to add a new product to the inventory.
def add_product(stock):
    show_available_products(stock) # Displays current inventory
    while True:
        # Request the name of the product to add
        name = input("Enter the name of the produc you want to add: ").strip().capitalize()
        if not name:  # Check that the name is not empty
            print("The name cannot be empty.")
            continue
        if not name.replace(" ", "").isalpha(): # Make sure the name only has letters
            print("The product name can only have letters.")
            continue
        if any(product['name'] == name for product in stock): # Check if the product is already in inventory
            print(f"The product '{name}' is already in inventory.")
            continue
        try:
            # Request the price and quantity of the new product
            price = float(input("Enter the price of the product: "))
            amount = int(input("Enter the quantity of the product: "))
            
            # If either price or quantity is negative, throw an error
            if price < 0 or amount < 0:
                raise ValueError
            # Add the product to inventory
            stock.append({"name": name, "price": price, "amount": amount})
            print(f"The product '{name}' has been added successfully.")
            show_available_products(stock)
        except ValueError:
            # If the price or quantity is invalid (for example, text is entered instead of numbers), display an error
            print("Price and quantity must be positive numbers.")
        # Ask if you want to enter another product
        wanna_continue = input("Do you want to enter another product? (Y/N): ").strip().upper()
        if wanna_continue != 'Y': # If you don't want to add another product, exit the loop
            break

# Function to query a product in the inventory by its name.
def search_product(stock):
    show_available_products(stock)# Displays current inventory
    name = input("Enter the name of the product you want to search for: ").strip().capitalize()
    if not name: # Check that the name is not empty
        print("The name cannot be empty.")
        return
    product_found = False
    for product in stock:
        if product['name'] == name: # Search for the product by name
            print(f"Product: {product['name']} - Price: {product['price']} - Amount: {product['amount']}")
            product_found = True
            break # Exits the loop when it finds the product
    if not product_found: # If the product is not in inventory
        print(f"The product {name} is out of stock. Here are the available products:")
        show_available_products(stock)

# Function to update the price of an existing product.
def update_product(stock):
    show_available_products(stock)# Displays current inventory
    name = input("Enter the name of the product you want to update: ").strip().capitalize()
    if not name: # Check that the name is not empty
        print("The name cannot be empty")
        return
    for product in stock:
        if product['name'] == name: # Search for the product by name
            try:
                new_price = float(input("Enter the new price of the product: "))
                new_amount = int(input("Enter the new quantity of the product: "))
                if new_price < 0 or new_amount < 0: # Check that the price and quantity are positive
                    raise ValueError
                product['price'] = new_price # Update the product price
                product['amount'] = new_amount # Update the product amount
                print(f"The product '{name}' has been successfully updated.")
                print(f"New price: {new_price}, New quantity: {new_amount}")
                return
            except ValueError:
               print("The price and quantity must be a positive number.")
    print(f"El producto '{name}' no está en el inventario.") # Si el producto no está, muestra un mensaje

# Function to remove a product from inventory.
def delete_product(stock):
    show_available_products(stock) # Displays current inventory
    name = input("Enter the name of the product you want to delete: ").strip().capitalize()
    if not name: # Check that the name is not empty
        print("The name cannot be empty")
        return
    product_found = False
    for product in stock:
        if product['name'] == name: # Search for the product by name
            product_found = True
            confirmacion = input(f"¿Are you sure you want to delete the product '{name}'? (Y/N):").strip().upper()
            if confirmacion == 'Y': #If the user confirms, the product is deleted.
                stock.remove(product)
                print(f"The product '{name}' has been removed.")
                show_available_products(stock)
            else:
                print(f"The deletion of product '{name}' has been cancelled.")
            break
    if not product_found: # If the product is not in inventory, print a message
        print(f"The product '{name}' is not in stock.")

# Function to calculate the total value of the inventory (price * quantity of each product).
def calculate_inventory_value(stock):
    # Function to calculate the total value of the inventory
    total = sum(product['price'] * product['amount'] for product in stock)
    print(f"The total value of the inventory is: {total:,.2f} USD") # Displays the total value

# Main function that controls the flow of the program.
def start_program():
    while True:
        show_menu() # Displays the menu with the options
        # Ask the user to choose an option

        # Verify that the option is a valid number between 1 and 6
        option = input("Choose one option (1-6): ").strip()
        if not option.isdigit() or not (1 <= int(option) <= 6):
            print("Incorrect option. You must enter a valid number (1-6).")
            continue
        if option == '1': 
            add_product(stock) # Call the function to add a product
        elif option == '2': 
            search_product(stock) # Call the function to search a product
        elif option == '3': 
            update_product(stock) # Call the function to update the price & amount of a product
        elif option == '4': 
            delete_product(stock) # Call the function to delete a product
        elif option == '5': 
            calculate_inventory_value(stock) # Call the function to calculate the total of the stock value
        elif option == '6': 
            print("Finalizing the program. . .") # Exit the program
            break

# Start the program
start_program()
