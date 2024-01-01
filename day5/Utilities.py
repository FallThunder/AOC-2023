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

def extract_seeds(input_str):
    # Define the pattern for extracting seed numbers
    pattern = r'seeds:\s*([\d\s]+)'

    # Use regular expression to find matches
    match = re.search(pattern, input_str)

    if match:
        # Extract and return the seed numbers as a list of integers
        seed_numbers = [int(num) for num in match.group(1).split()]
        return seed_numbers

    else:
        # Return an empty list if no match is found
        return []
    
def extract_map(map_name, lines):
    """
    Extract the map from the input lines for the specific map_name.

    Parameters:
    - map_name (str): The name of the map to extract.
    - lines (list of str): The list of strings to extract the map from.

    Returns:
    - list of tuples: A list of tuples, where each tuple contains destination, source and range.
    """
    extracted_map = []

    # Flag to indicate whether the current line is part of the desired map
    is_desired_map = False

    # Iterate through each line in the list
    for line in lines:
        # Check if the line starts with the desired map_name
        if line.startswith(map_name):
            is_desired_map = True

        elif is_desired_map and not line.strip():  # Stop when an empty line is encountered
            break

        elif is_desired_map:
            # Extract destination, source, and range from the line
            destination, source, range_value = map(int, line.split())
            
            # Append the extracted values as a tuple to the result list
            extracted_map.append((destination, source, range_value))

    return extracted_map

def get_destination(source, map):
    """
    Get the destination for the given source from the map.

    Parameters:
    - source (int): The source value to find the destination for.
    - map (list of tuples): The map to use for finding the destination.

    Returns:
    - int: The destination value for the given source.
    """
    # Iterate through each tuple in the map
    for destination, source_value, range_value in map:
        # Check if the source value is within the range of the current tuple
        if source_value <= source < source_value + range_value:
            # Return the destination value
            return source + destination - source_value

    # Return -1 if no destination is found
    return source

def seed_range(seed_list):
    result = []
    index = 0

    for i in seed_list:
        if index % 2 == 0:
            for l in range(i, i+seed_list[index+1]):
                result.append(l)

        index += 1

    return result

def get_source(destination, map):
    """
    Get the initial source for the given destination from the map.

    Parameters:
    - destination (int): The destination value to find the initial source for.
    - map (list of tuples): The map to use for finding the initial source.

    Returns:
    - int: The initial source value for the given destination.
    """
    # Iterate through each tuple in the map
    for destination_value, source_value, range_value in map:
        # Check if the destination value is within the range of the current tuple
        if destination_value <= destination < destination_value + range_value:
            # Return the initial source value
            return destination - destination_value + source_value

    # Return -1 if no initial source is found
    return destination

def process_ranges(numbers, number_to_check):
    def parse_ranges(numbers):
        ranges = [(numbers[i], numbers[i] + numbers[i + 1]) for i in range(0, len(numbers), 2)]
        return ranges

    def is_in_ranges(number, ranges):
        for start, end in ranges:
            if start <= number <= end:
                return True
        return False

    ranges = parse_ranges(numbers)
    result = is_in_ranges(number_to_check, ranges)

    return result