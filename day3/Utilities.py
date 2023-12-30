def read_file_to_list(file_path):
    """
    Read the contents of a file into a list of strings.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - list of str: A list of strings, where each string represents a line in the file.
    """
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file into a list
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def extract_next_number(input_string, start_position):
    """
    Extract the next non-negative integer from the input string starting at the given position.

    Parameters:
    - input_string (str): The input string containing characters and numbers.
    - start_position (int): The starting position to begin searching for the next number.

    Returns:
    - tuple: A tuple containing the extracted non-negative integer and the ending position of the number.
             If no number is found, returns (None, -1).
    """
    length = len(input_string)
    number = ''

    # Find the starting position of the number
    while start_position < length and not input_string[start_position].isdigit():
        start_position += 1

    # Extract the number
    while start_position < length and input_string[start_position].isdigit():
        number += input_string[start_position]
        start_position += 1

    # Return the result
    if number:
        return int(number), start_position
    else:
        return None, -1
    

def has_special_characters(input_string, start_position, end_position):
    """
    Check if there are any special characters within the specified substring.

    Parameters:
    - input_string (str): The input string.
    - start_position (int): The starting position of the substring.
    - end_position (int): The ending position of the substring.

    Returns:
    - bool: True if there are special characters, False otherwise.
    """
    substring = input_string[start_position:end_position]
    
    for char in substring:
        if not (char.isdigit() or char == '.'):
            # Found a special character
            return True

    # No special characters found
    return False
