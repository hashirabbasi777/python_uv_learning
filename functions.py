#In this code we type the function to calculate two numbers

def add_numbers(a, b):
    """
    Function to add two numbers and print the result
    Parameters:
        a: first number
        b: second number
    """
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    return result

# Example usage
if __name__ == "__main__":
    add_numbers(5, 3)  # This will print: The sum of 5 and 3 is: 8
