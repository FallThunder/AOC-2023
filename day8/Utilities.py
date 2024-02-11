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
    
def create_map(paths):
    """
    Create a dictionary that maps the first three letters of a path to the next two steps.
    
    Parameters:
    - paths (list of str): A list of strings, where each string represents a path.
    
    Returns:
    - dict: A dictionary that maps the first three letters of a path to the next two steps.
    """
    # Create a dictionary to store the paths
    dict = {}
    # Iterate through the paths
    for i in paths:
        # Get the first three letters of the path
        key = i[0:3]
        # Get the next two steps
        value = (i[7:10], i[12:15])
        # Add the key-value pair to the dictionary
        dict[key] = value

    return dict

def trace_path(step_data, map):
    """
    Trace the path of the robot.
    
    Parameters:
    - step_data (tuple): A tuple that stores the current step, the steps, and the current index.
    
    Returns:
    - tuple: A tuple that stores the next step, the steps, and the current index.
    """
    # Get the current step
    step = step_data[2]
    # Get the position of the next step
    pos = int(step_data[1][step])
    # Get the next step
    new_step_data = (map[step_data[0]][pos], step_data[1])
    # Increment the current step by 1
    step += 1
    # If the current step is less than the length of the steps
    if step < len(step_data[1]):
        # Add the current step to the tuple
        new_step_data += (step,)

    else:
        # Add 0 to the tuple
        new_step_data += (0,)

    return new_step_data

def start_paths(lines):
    """
    Create a list of starting nodes.
    
    Parameters:
    - lines (list of str): A list of strings, where each string represents a path.
    
    Returns:
    - list of str: A list of strings, where each string represents a starting node.
    """
    # Create a list to store the starting nodes
    starting_nodes = []

    # Iterate through the paths
    for node_list in lines:
        # If the path ends with A
        if node_list[2] == 'A':
            # Add the letters of the path to the list
            starting_nodes.append(node_list[:3])

    return starting_nodes