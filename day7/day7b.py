from operator import itemgetter
from Utilities import read_file_to_list
from UtilitiesB import adjust_hand
from UtilitiesB import classify_hand
from UtilitiesB import rank_cards

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day7/day7.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    # Create a list to store the hands
    hand_list = []
    # Create a variable to store the final score
    final = 0
    # iterate through each hand
    for hand in lines:
        # Store the cards and bid pair in a tuple
        hand_data = (hand.split()[0], hand.split()[1])
        # Add an element to the tuple where J cards are replaced with the most common non J card
        hand_data = adjust_hand(hand_data)
        # Classify the hand and add the classification to the tuple
        hand_data = classify_hand(hand_data)
        # Rank the cards and add the rank to the tuple
        hand_data = rank_cards(hand_data)
        # Add the hand to the hand_list
        hand_list.append(hand_data)

    # Sort the hand_list by rank
    hand_list = sorted(hand_list, key=itemgetter(4))

    # Iterate through each hand in the hand_list
    for hand in hand_list:
        # Calculate the final score using the current position in the list multiplied by the bid
        final += (hand_list.index(hand) + 1) * int(hand[1])

    # Print the final score
    print(final)

if __name__ == "__main__":
    main()