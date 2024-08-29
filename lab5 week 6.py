item_id_counter = 1000

def add_inventory_item():
    global item_id_counter
    
    # Generate a unique Item ID
    item_id = item_id_counter
    item_id_counter += 1
    
    # Prompt for user inputs
    item_name = input("Enter the Item Name: ")
    quantity = int(input("Enter the Quantity: "))
    price_per_item = input(input("Enter the Price per Item: "))
    
    # Return all the collected details including the generated Item ID
    return {
        'Item Name': item_name,
        'Item ID': item_id,
        'Quantity': quantity,
        'Price per Item': price_per_item
    }

# Example usage
if __name__ == "__main__":
    item_details = add_inventory_item()
    print(item_details)


item_id_counter = 1000
def add_inventory_item():
    global item_id_counter
    
    # Generate a unique Item ID
    item_id = item_id_counter
    item_id_counter += 1
    
    # Prompt for user inputs
    item_name = input("Enter the Item Name: ")
    quantity = int(input("Enter the Quantity: "))
    price_per_item = input(input("Enter the Price per Item: "))

    
    # Return all the collected details including the generated Item ID
    return {
        'Item Name': item_name,
        'Item ID': item_id,
        'Quantity': quantity,
        'Price per Item': price_per_item
    }

def calculate_total_value():
    # Call add_inventory_item to get the item details
    item_details = add_inventory_item()
    
    # Extract quantity and price per item from the returned dictionary
    quantity = item_details['Quantity']
    price_per_item = item_details['Price per Item']
    
    # Calculate the total value
    total_value = quantity * price_per_item
    
    # Return the computed total value
    return total_value

# Example usage
if __name__ == "__main__":
    total_value = calculate_total_value()
    print(f"The total value of the inventory for the item is: ${total_value:.2f}")



    # Global inventory store
inventory = {}

# Global counter for Item IDs
item_id_counter = 1000

def add_inventory_item():
    global item_id_counter, inventory
    
    # Generate a unique Item ID
    item_id = item_id_counter
    item_id_counter += 1
    
    # Prompt for user inputs
    item_name = input("Enter the Item Name: ")
    quantity = int(input("Enter the Quantity: "))
    price_per_item = float(input("Enter the Price per Item: "))
    
    # Store the item in inventory
    inventory[item_id] = {
        'Item Name': item_name,
        'Quantity': quantity,
        'Price per Item': price_per_item
    }
    
    # Return all the collected details including the generated Item ID
    return {
        'Item Name': item_name,
        'Item ID': item_id,
        'Quantity': quantity,
        'Price per Item': price_per_item
    }

def update_inventory(item_id):
    global inventory
    
    # Check if the item exists in the inventory
    if item_id in inventory:
        # Prompt for new details
        new_quantity = int(input("Enter the new Quantity: "))
        new_price_per_item = float(input("Enter the new Price per Item: "))
        
        # Update the inventory item
        inventory[item_id]['Quantity'] = new_quantity
        inventory[item_id]['Price per Item'] = new_price_per_item
        
        return f"Item ID {item_id} has been updated successfully."
    else:
        # Return a message if item is not found
        return f"Item ID {item_id} not found."

# Example usage
if __name__ == "__main__":
    # Add an item to demonstrate the update functionality
    add_inventory_item()
    
    # Update the item
    item_id_to_update = int(input("Enter the Item ID to update: "))
    result = update_inventory(item_id_to_update)
    print(result)
