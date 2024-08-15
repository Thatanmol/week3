# Author Sana Alyaseri
# class: software Development
# Example 6: function where one function calls another to take the result and do futher processing.

def add(a, b):
    return a + b 

def multiply(x, y):
    return x * y

def add_and_multiply(a, b, c):
    sum_result = add(a, b) # Calling the multiply function
    product_result = multiply(sum_result, c)  # calling the multiply function
    return product_result


result = add_and_multiply(2, 3, 4)
print(result) # output: 20