from Utilities import read_file_to_list
from Utilities import create_map
from Utilities import trace_path

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day8/day8.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    # Store the steps in a list where each step is represented by a 0 or 1
    steps = [step for step in lines[0].replace('L', '0').replace('R', '1')]
    # Create a variable to store the current step
    current_step = "AAA"
    # Create a dictionary to store the potential paths
    map = create_map(lines[2:])
    # Create a tuple that stores the current step and the next step from steps
    step_data = (current_step, steps, 0)
    # Set found_ZZZ to False
    found_ZZZ = False
    # Create a variable to store the final number of steps
    final = 0
    # While ZZZ has not been found
    while not found_ZZZ:
        # Find the next step
        step_data = trace_path(step_data, map)
        # If the next step is ZZZ
        if step_data[0] == "ZZZ":
            # Set found_ZZZ to True
            found_ZZZ = True

        # Increment final by 1
        final += 1

    print(final)

if __name__ == "__main__":
    main()