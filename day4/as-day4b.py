# Day 4 Main Program
from Utilities import read_file_to_list
from Utilities import extract_card_parts
from Utilities import get_winners

def main():
    # Path to input data
    file_path = 'AOC 2023/Day 4/day4.txt'

    # Convert file content to a list of strings
    lines = read_file_to_list(file_path)

    # Initialize list with number of each card as 1
    number_of_cards = [1] * len(lines)

    # Process each line
    for line in lines:
        # Extract card number and the two sets of numbers to compare
        parts = extract_card_parts(line)
           
        # Find number of winners
        winners = get_winners(parts[1], parts[2])
   
        # For x number of winners, append the next x cards to lines.
        for x in range(winners):
            lines.append(lines[parts[0]+x])

    # Print the number of cards
    print(len(lines))

if __name__ == "__main__":
    main()
