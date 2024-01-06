from Utilities import read_file_to_list
from Utilities import time_and_record
from Utilities import find_answer

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day6/day6.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    # Extract time and record data from the input data
    t_and_r = time_and_record(lines)
    # Find the answer
    final_answer = find_answer(t_and_r)
    # Print the answer
    print(final_answer)

if __name__ == "__main__":
    main()