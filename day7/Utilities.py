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
    
def hand_type(card_and_bid):
    """
    Find the type of hand.
    
    Parameters:
    - card_and_bid (list of str): A list of strings, where each string represents a line in the file.
    
    Returns:
    - None: Prints the type of hand.
    """
    hand_dict = {}

    # List of cards
    cards = [
        "2", "3",
        "4", "5",
        "6", "7",
        "8", "9",
        "T", "J",
        "Q", "K",
        "A"
    ]
    # Iterate through each hand
    for hand in card_and_bid:
        hand_repeat = []
        
        # Iterate through each card type
        for card_type in cards:
            repeat_count = hand[:5].count(card_type)

            # If the card type is not present in the hand, continue
            if repeat_count > 0:
                hand_repeat.append((card_type, repeat_count))
            
        # Sort the hand_repeat list in descending order of the number of times the card type is repeated
        hand_repeat = sorted(hand_repeat, key=lambda card_repeat: card_repeat[1], reverse = True)
        
        # Analyze the length of hand_repeat to determine the type of hand
        if len(hand_repeat) == 5:
            hand_dict[hand] = 100
            resolve_rank(hand_dict)
        
        elif len(hand_repeat) == 4:
            if hand_repeat[0][1] == 2:
                hand_dict[hand] = 200
                resolve_rank(hand_dict)

        elif len(hand_repeat) == 3:
            if hand_repeat[0][1] == 2:
                hand_dict[hand] = 300
                resolve_rank(hand_dict)

            else:
                hand_dict[hand] = 400
                resolve_rank(hand_dict)

        elif len(hand_repeat) == 2:
            if hand_repeat[0][1] == 3:
                hand_dict[hand] = 500
                resolve_rank(hand_dict)

            else:
                hand_dict[hand] = 600
                resolve_rank(hand_dict)

        else:
            hand_dict[hand] = 700
            resolve_rank(hand_dict)

    # Sort the hand_dict in ascending order of the hand type
    hand_dict = sorted(hand_dict.items(), key=lambda x:x[1])

    return hand_dict

def resolve_rank(hand_and_rank):
    """
    Resolve the rank of the hand.
    
    Parameters:
    - hand_and_rank (list of tuple): A list of tuples, where each tuple represents a hand and its rank.
    
    Returns:
    - None: Prints the rank of the hand.
    """
    print(hand_and_rank)