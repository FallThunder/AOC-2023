def readFileToList(filePath):
    """
    Read the contents of a file into a list of strings.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - list of str: A list of strings, where each string represents a line in the file.
    """
    try:
        with open(filePath, 'r') as file:
            # Read all lines from the file into a list
            lines = file.read().split('\n')
            return lines

    except FileNotFoundError:
        print(f"Error: File not found at {filePath}")
        return []

    except Exception as e:
        print(f"Error: {e}")
        return []
    
def initialSequence(line):
    """
    Create a sequence from a string.

    Parameters:
    - line (str): The string to be converted into a sequence.

    Returns:
    - list of int: A list of integers representing the sequence.
    """
    # Split the string by the delimiter ' '
    sequence = line.split(' ')
    # Convert each element to an integer and store it in a list
    sequence = [int(num) for num in sequence]

    return sequence

def reduceSequence(sequence):
    """
    Solve a sequence.
    
    Parameters:
    - sequence (list of int): The sequence to be solved.
    
    Returns:
    """
    # Create an empty list to store the solved sequence
    solvedSequence = []
    # Set the position to 0
    pos = 0

    # Go through each number in the sequence
    for num in sequence:
        # Try to subtract the current number from the next number in the sequence
        try:
            solvedSequence.append(sequence[pos + 1] - num)

        except:
            pass

        pos += 1

    return solvedSequence

def solveSequence(sequenceMap):
    """
    Solve a sequence map.
    
    Parameters:
    - sequenceMap (list of list of int): The sequence map to be solved.
    
    Returns:
    - int: The solution to the sequence map.
    """
    # Go through each sequence in the sequence map
    for sequence in sequenceMap:
        # Try to add the last number in the current sequence to the last number in the next sequence
        try:
            sequenceMap[sequenceMap.index(sequence) + 1] += [sequence[-1] + sequenceMap[sequenceMap.index(sequence) + 1][-1]]
        
        # If there is no next sequence, break the loop
        except:
            pass

    # Return the last number in the last sequence
    return sequenceMap[-1][-1]

def solveSequenceB(sequenceMap):
    """
    Solve a sequence map.
    
    Parameters:
    - sequenceMap (list of list of int): The sequence map to be solved.
    
    Returns:
    - int: The solution to the sequence map.
    """
    # Go through each sequence in the sequence map
    for sequence in sequenceMap:
        # Try to add the first number in the current sequence to the first number in the next sequence
        try:
            sequenceMap[sequenceMap.index(sequence) + 1] = [sequenceMap[sequenceMap.index(sequence) + 1][0] - sequence[0]] + sequenceMap[sequenceMap.index(sequence) + 1]
        
        # If there is no next sequence, break the loop
        except:
            pass

    # Return the first number in the last sequence
    return sequenceMap[-1][0]