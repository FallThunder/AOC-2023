import numpy as np

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
    
def time_and_record_parta(input_list):
    """
    Extracts vertically corresponding numbers from a formatted input list.

    Parameters:
    - input_list (list): A string containing formatted time and distance data.

    Returns:
    - list of tuples: A list containing tuples of vertically corresponding
      time and distance values extracted from the input list.
    """
    # Extract time values from the second element of the first line
    time_line = input_list[0].split()[1:]
    time_values = [int(value) for value in time_line]

    # Extract distance values from the second element of the second line
    distance_line = input_list[1].split()[1:]
    distance_values = [int(value) for value in distance_line]

    # Combine time and distance values into a list of tuples
    result = list(zip(time_values, distance_values))

    # Return the resulting list
    return result

def calculate_timings_parta(input_list):
    """
    Finds the answer to the question.
    
    Parameters:
    - input_list (list): A list containing tuples of vertically corresponding
      time and distance values extracted from the input list.
      
    Returns:
    - int: The answer to the question.
    """
    # Create a list to store the answer count for each time and record pair
    answer_count_list = []

    # Iterate through each time and record pair
    for time, record in input_list:
        answer_count = 0

        # Iterate through each possible time to hold the record
        for t_to_hold in range(1, time + 1):
            # If the time to hold the record is less than the current time,
            if t_to_hold * (time - t_to_hold) > record:
                answer_count += 1

        # Add the answer count to the answer count list
        answer_count_list.append(answer_count)

    # Find the product of all the answer counts
    answer = np.prod(answer_count_list)

    # Return the answer
    return answer

def time_and_record_partb(input_list):
    """
    Concatenates time values into a single large integer and
    distance values into another large integer from a list of formatted strings.

    Parameters:
    - input_list (list of str): A list containing formatted time and distance data.

    Returns:
    - tuple: A tuple containing two integers - the concatenated time value
      and the concatenated distance value.
    """
    # Extract and join time values into a single integer
    time_line = input_list[0].split()[1:]
    time_value = int(''.join(time_line))

    # Extract and join distance values into a single integer
    distance_line = input_list[1].split()[1:]
    distance_value = int(''.join(distance_line))

    # Return a tuple with the concatenated time and distance values
    return time_value, distance_value

def calculate_timings_partb(input_list):
    """
    Finds the answer to the question.
    
    Parameters:
    - input_list (list): A list containing tuples of vertically corresponding
      time and distance values extracted from the input list.
      
    Returns:
    - int: The answer to the question.
    """
    # Extract time and record values from the input list
    time = input_list[0]
    record = input_list[1]
    answer_count = 0

    # Iterate through each possible time to hold the record
    for t_to_hold in range(1, time + 1):
        # If the time to hold the record is less than the current time,
        if t_to_hold * (time - t_to_hold) > record:
            answer_count += 1

    # Return the answer
    return answer_count