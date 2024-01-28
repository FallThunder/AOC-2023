def adjust_hand(input_tuple):
    """
    Replace all 'J' cards with the most common non 'J' card in the set of cards.

    Parameters:
    - input_tuple (tuple): The input tuple.

    Returns:
    - tuple: The adjusted tuple.
    """
    # Extract the hand from the input tuple
    hand = input_tuple[0]
    # If 'J' appears 5 times, return the original hand
    if hand.count('J') == 5:
        input_tuple += (hand,)
        return input_tuple

    # Create a dictionary to count the occurrence of each card
    card_count = {card: hand.count(card) for card in set(hand) if card != 'J'}
    # Find the card with the highest count
    max_card = max(card_count, key=card_count.get)
    # Replace 'J' with the card with the highest count
    adjusted_hand = (card if card != 'J' else max_card for card in hand)
    # Convert the adjusted hand to a string
    adjusted_hand_str = ''.join(adjusted_hand)
    # Add the adjusted hand string as a new element in the input tuple
    input_tuple += (adjusted_hand_str,)

    return input_tuple

def classify_hand(input_tuple):
    """
    Classify the hand.
    
    Parameters:
    - input_tuple (tuple): The input tuple.
    
    Returns:
    - tuple: The input tuple with the classification.
    """

    # Check if the hand is a five of a kind
    if check_if_five_of_a_kind(input_tuple[2]):
        # Add the classification to the tuple
        input_tuple += (7,)
        return input_tuple
    
    # Check if the hand is a four of a kind
    elif check_if_four_of_a_kind(input_tuple[2]):
        # Add the classification to the tuple
        input_tuple += (6,)
        return input_tuple
    
    # Check if the hand is a full house
    elif check_if_full_house(input_tuple[2]):
        # Add the classification to the tuple
        input_tuple += (5,)
        return input_tuple
    
    # Check if the hand is a three of a kind
    elif check_if_three_of_a_kind(input_tuple[2]):
        # Add the classification to the tuple
        input_tuple += (4,)
        return input_tuple
    
    # Check if the hand is a two pair
    elif check_if_two_pair(input_tuple[2]):
        # Add the classification to the tuple
        input_tuple += (3,)
        return input_tuple
    
    # Check if the hand is a one pair
    elif check_if_one_pair(input_tuple[2]):
        # Add the classification to the tuple
        input_tuple += (2,)
        return input_tuple
    
    # If the hand is none of the above, it is a high card
    else:
        # Add the classification to the tuple
        input_tuple += (1,)
        return input_tuple

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

def rank_cards(input_tuple):
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
    rank = (input_tuple[3] * (15**5) + card_values[input_tuple[0][0]] * (15**4) + card_values[input_tuple[0][1]] * (15**3) + card_values[input_tuple[0][2]] * (15**2) + card_values[input_tuple[0][3]] * (15**1) + card_values[input_tuple[0][4]])
    input_tuple += (rank,)
    return input_tuple