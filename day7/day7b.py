from Utilities import read_file_to_list
from Utilities import hand_type
from Utilities import adjust_hand

def main():
    list = []
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day7/day7.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    for hand in lines:
        # Adjust hand to account for jokers
        adjusted_hand = adjust_hand(hand)
        # Find the hand type
        list.append(hand_type(hand, adjusted_hand))

    # Sort the list by 2nd element in tuple in ascending order
    list.sort(key=lambda x: x[2], reverse=False)
    # Multiply the bid with the index + 1 of the hand and sum them up
    sum = 0
    for i in range(len(list)):
        sum += int(list[i][1]) * (i + 1)

    print(sum)

if __name__ == "__main__":
    main()