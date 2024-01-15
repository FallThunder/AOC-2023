from collections import OrderedDict

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
    
def hand_type(hand, adjusted_hand= -1):
    """
    Find the type of hand.
    
    Parameters:
    - card_and_bid (list of str): A list of strings, where each string represents a line in the file.
    
    Returns:
    - dict: A dictionary, where the key is the hand and the value is the rank of the hand.
    """
    # If adjusted_hand == -1, then set adjusted_hand to hand
    if adjusted_hand == -1:
        adjusted_hand = hand
        # Card values
        card_values = {
            "2": 2, "3": 3,
            "4": 4, "5": 5,
            "6": 6, "7": 7,
            "8": 8, "9": 9,
            "T": 10, "J": 11,
            "Q": 12, "K": 13,
            "A": 14
        }
        # Split the hand into cards and bid
        cards, bid = hand.split()

    else:
        # Card values
        card_values = {
            "J": 1, "2": 2,
            "3": 3, "4": 4,
            "5": 5, "6": 6,
            "7": 7, "8": 8,
            "9": 9, "T": 10,
            "Q": 12, "K": 13,
            "A": 14
        }
        # Split the hand into cards and bid
        cards = adjusted_hand.split()[0]
        bid = hand.split()[1]
    
    if not check_if_five_of_a_kind(cards):
        if not check_if_four_of_a_kind(cards):
            if not check_if_full_house(cards):
                if not check_if_three_of_a_kind(cards):
                    if not check_if_two_pair(cards):
                        if not check_if_one_pair(cards):
                            return (cards, bid, (1 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 1)
                        else:
                            return (cards, bid, (2 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 2)
                    else:
                        return (cards, bid, (3 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 3)
                else:
                    return (cards, bid, (4 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 4)
            else:
                return (cards, bid, (5 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 5)
        else:
            return (cards, bid, (6 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 6)
    else:
        return (cards, bid, (7 * (14**5) + card_values[cards[0]] * (14**4) + card_values[cards[1]] * (14**3) + card_values[cards[2]] * (14**2) + card_values[cards[3]] * (14**1) + card_values[cards[4]] * (14**0)), 7)

def check_if_five_of_a_kind(hand):
    """
    Check if the hand is a five of a kind.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - bool: True if the hand is a five of a kind, False otherwise.
    """

    # Check if the hand is a five of a kind
    for card in hand:
        if hand.count(card) == 5:
            return True

    return False

def check_if_four_of_a_kind(hand):
    """
    Check if the hand is a four of a kind.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - bool: True if the hand is a four of a kind, False otherwise.
    """

    # Check if the hand is a four of a kind
    for card in hand:
        if hand.count(card) == 4:
            return True

    return False

def check_if_full_house(hand):
    """
    Check if the hand is a full house.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - bool: True if the hand has 3 cards of one type and 2 of another, False otherwise.
    """

    # Check if the hand is a full house
    for card in hand:
        if hand.count(card) == 3:
            for card in hand:
                if hand.count(card) == 2:
                    return True

    return False

def check_if_three_of_a_kind(hand):
    """
    Check if the hand is a three of a kind.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - bool: True if the hand is a three of a kind, False otherwise.
    """
    
    # Check if the hand is a three of a kind
    for card in hand:
        if hand.count(card) == 3:
            return True

    return False

def check_if_two_pair(hand):
    """
    Check if the hand is a two pair.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - bool: True if the hand is a two pair, False otherwise.
    """

    first_pair = ""
    # Check if the hand is a two pair
    for card in hand:
        if hand.count(card) == 2:
            first_pair = card
            for card in hand:
                if hand.count(card) == 2 and not card == first_pair:
                    return True

    return False

def check_if_one_pair(hand):
    """
    Check if the hand is a one pair.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - bool: True if the hand is a one pair, False otherwise.
    """

    # Check if the hand is a one pair
    for card in hand:
        if hand.count(card) == 2:
            return True

    return False

def adjust_hand(hand):
    """
    Replace any occurrence of 'J' with the card that repeats the most and has the highest value in the card_values dictionary.
    
    Parameters:
    - hand (str): The hand.
    
    Returns:
    - str: The hand with 'J' replaced.
    """
    # Card values
    card_values = {
        "J": 1, "2": 2,
        "3": 3, "4": 4,
        "5": 5, "6": 6,
        "7": 7, "8": 8,
        "9": 9, "T": 10,
        "Q": 12, "K": 13,
        "A": 14
    }
    # Pull the hand out of the line
    hand = hand.split()[0]
    # If 'J' appears 5 times, return the original hand
    if hand.count('J') == 5:
        return hand
    # Create a dictionary to count the occurrence of each character
    char_count = {char: hand.count(char) for char in set(hand) if char != 'J'}
    # Find the character with the highest count and the highest value
    max_char = max(char_count, key=lambda char: (char_count[char], card_values[char]))
    # Replace 'J' with the character with the highest count and the highest value
    adjusted_hand = hand.replace('J', max_char)

    return adjusted_hand