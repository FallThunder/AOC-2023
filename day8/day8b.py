from Utilities import read_file_to_list
from Utilities import create_map
from Utilities import trace_path
from Utilities import start_paths
import math

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day8/day8.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    # Store the steps in a list where each step is represented by a 0 or 1
    steps = [step for step in lines[0].replace('L', '0').replace('R', '1')]
    # Call start_paths to get the starting nodes
    starting_nodes = start_paths(lines[2:])
    # Create a dictionary to store the potential paths
    map = create_map(lines[2:])

    # Create a list to store data on each path
    step_data = []

    # For each starting node
    for node in starting_nodes:
        # Create a tuple that stores the current step, possible steps and the next step from steps
        step_data.append((node, steps, 0))
    
    # Set on_Z to False
    on_Z = False

    # Create a variable to store the number of rounds
    rounds = 0

    # Store the number of rounds for each path to reach Z
    num_rounds = []
    
    while not on_Z:
        # Create a list to store the new step data
        new_step_data = []
        # For each tuple_set in step_data
        for tuple_set in step_data:
            # Call trace_path to get the next step
            tuple_set = trace_path(tuple_set, map)
            # If the current step is not Z
            new_step_data.append(tuple_set)
        
        # Set step_data to new_step_data
        step_data = new_step_data

        # Increment rounds by 1
        rounds += 1

        # If step_data is empty
        if len(step_data) == 0:
            # Set on_Z to True
            on_Z = True
        
        # For each tuple_set in step_data
        for tuple_set in step_data:
            # If the current step is Z
            if tuple_set[0][2] == 'Z':
                # Append the number of rounds to num_rounds
                num_rounds.append(rounds)
                # Remove the tuple_set from step_data
                step_data.remove(tuple_set)

    # Print the LCM of the number of rounds
    print(math.lcm(*num_rounds))

if __name__ == "__main__":
    main()