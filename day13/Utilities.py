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

def extractPatterns(lines):
    """
    Extract patterns from a list of strings.
    
    Parameters:
    - lines (list of str): A list of strings, where each string represents a line in the file.
    
    Returns:
    - list of list of str: A list of lists of strings, where each list of strings represents a pattern.
    """
    # Create an empty list to store the patterns
    patterns = []
    # Split the list of strings into a list of lists of strings, where each list of strings represents a pattern
    while '' in lines:
        patterns.append(lines[0:lines.index('')])
        lines = lines[lines.index('')+1:]

    # Add the last pattern to the list of patterns
    patterns.append(lines)

    return patterns

def findHorizontalMirror(pattern):
    """
    Find the horizontal mirror of a pattern.

    Parameters:
    - pattern (list of str): A list of strings, where each string represents a line in the pattern.

    Returns:
    - tuple: A tuple containing the original pattern, the type of mirror, and the line number at which the mirror is found.
    """
    # For each line in the pattern
    for line in range(len(pattern)):
        # If line is within the length of the pattern
        if line + 1 < len(pattern):
            # If the current line is the same as the next line
            if pattern[line] == pattern[line + 1]:
                # If the start of the pattern up to the current line is the same as the end of the pattern from the next line
                if set(pattern[:line + 1]).issubset(pattern[line + 1:][::-1]) or set(pattern[:line + 1]).issuperset(pattern[line + 1:][::-1]):
                    # Return the original pattern, the type of mirror, and the line number at which the mirror is found
                    return (pattern, "H", len(pattern[:line + 1]))

            else:
                continue

        else:
            return (pattern, "H", 0)

def findVerticalMirror(pattern):
    """
    Find the horizontal mirror of a pattern.

    Parameters:
    - pattern (list of str): A list of strings, where each string represents a line in the pattern.

    Returns:
    - tuple: A tuple containing the original pattern, the type of mirror, and the line number at which the mirror is found.
    """
    # Create an empty list to store the rotated pattern
    rotatedPattern = []
    # For each line in the pattern
    for patternLine in zip(*pattern):
        # Rotate the pattern line
        patternLine = ''.join(patternLine)
        # Add the rotated pattern to the list of rotated patterns
        rotatedPattern.append(patternLine)
    # For each line in the pattern
    for line in range(len(rotatedPattern)):
        # If line is within the length of the pattern
        if line + 1 < len(rotatedPattern):
            # If the current line is the same as the next line
            if rotatedPattern[line] == rotatedPattern[line + 1]:
                # If the start of the pattern up to the current line is the same as the end of the pattern from the next line
                if set(rotatedPattern[:line + 1]).issubset(rotatedPattern[line + 1:][::-1]) or set(rotatedPattern[:line + 1]).issuperset(rotatedPattern[line + 1:][::-1]):
                    # Return the original pattern, the type of mirror, and the line number at which the mirror is found
                    return (rotatedPattern, "V", len(rotatedPattern[:line + 1]))

            else:
                continue

        else:
            return (rotatedPattern, "V", 0)

def scorePattern(patternData):
    """
    Score a pattern.
    
    Parameters:
    - patternData (tuple): A tuple containing the original pattern, the type of mirror, and the line number at which the mirror is found.

    Returns:
    - int: The score of the pattern.
    """
    if patternData[1] == "H":
        return patternData[2] * 100
    
    else:
        return patternData[2]