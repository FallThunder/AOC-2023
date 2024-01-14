from Utilities import read_file_to_list
from Utilities import hand_type
from Utilities import resolve_rank
from Utilities import total_winnings

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day7/day7.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    # Find the hand type
    hand_and_rank = hand_type(lines)
    # Resolve any duplicate rankings
    hand_and_rank = resolve_rank(hand_and_rank)
    # Total the winnings, rank * bid
    winnings = total_winnings(hand_and_rank)
    print(winnings)

if __name__ == "__main__":
    main()