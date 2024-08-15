# Auther Sana Alyaseri
# Class: Software Development
# Example 4: Accessing a Global Variable 
count = 0 
def increment():
    global count # Declare 'count' as global
    count += 1 
    print(f"count inside function: {count}")

    # Call the function
    increment()
    increment()
    
    # Access the global variable
    print(f"count outside function: {count}")
    