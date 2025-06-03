name = "John"
age = 20

print(f"Hello, {name}! You are {age} years old.")

def delete_number(numbers_list, number_to_delete):
    """
    Delete a number from the list if it exists.
    
    Args:
        numbers_list (list): List of numbers
        number_to_delete: Number to delete from the list
        
    Returns:
        list: Updated list after deletion
    """
    if number_to_delete in numbers_list:
        numbers_list.remove(number_to_delete)
        print(f"Number {number_to_delete} has been deleted from the list.")
    else:
        print(f"Number {number_to_delete} is not in the list.")
    return numbers_list

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
numbers = delete_number(numbers, 3)
print("List after deletion:", numbers)
