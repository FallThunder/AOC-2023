import re

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
            lines = file.read().split('\n')
            return lines
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


import re

import re

def extract_card_parts(input_string):
    """
    Extract card number, first part of the card and the second part of the card.

    Parameters:
    - input_string (str): The input string containing contents of the card.

    Returns:
    - tuple: A tuple containing the card number (as an integer), list of numbers in the first part of the card, and a list of numbers in the second part of the card.
             If no number is found, returns (None, [], []).
    """
    
    # Extract card number
    card_number_match = re.search(r'Card\s+(\d+):', input_string)
    if card_number_match:
        card_number = int(card_number_match.group(1))
    else:
        card_number = None

    # Extract numbers before "|"
    numbers_before_pipe_match = re.search(r':\s*([^|]+)', input_string)
    if numbers_before_pipe_match:
        numbers_before_pipe = [int(num) for num in numbers_before_pipe_match.group(1).split()]
    else:
        numbers_before_pipe = []

    # Extract numbers after "|"
    numbers_after_pipe_match = re.search(r'\|\s*([^|]+)', input_string)
    if numbers_after_pipe_match:
        numbers_after_pipe = [int(num) for num in numbers_after_pipe_match.group(1).split()]
    else:
        numbers_after_pipe = []

    return card_number, numbers_before_pipe, numbers_after_pipe

def get_winners(list1, list2):
    """
    Count the number of common elements between two lists of integers.

    Parameters:
    - list1 (list): The first list of integers.
    - list2 (list): The second list of integers.

    Returns:
    - int: The number of common elements between the two lists.
    """
    common_elements = set(list1) & set(list2)
    return len(common_elements)


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

