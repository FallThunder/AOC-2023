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
                # Split the pattern into two slices
                fSlice = pattern[:line + 1]
                sSlice = pattern[line + 1:]
                # If the start of the pattern up to the current line is the same as the end of the pattern from the next line
                if set(fSlice).issubset(sSlice):
                    # If the reverse of the second slice is the same as the first slice up to the current line
                    if fSlice[::-1] == sSlice[:len(fSlice)]:
                        # Return the original pattern, the type of mirror, and the line number at which the mirror is found
                        return (pattern, "H", len(fSlice))
                
                # If the start of the pattern up to the current line is the same as the end of the pattern from the next line
                elif set(fSlice).issuperset(sSlice):
                    # If the reverse of the second slice is the same as the first slice up to the current line
                    if sSlice == fSlice[::-1][:len(sSlice)]:
                        # Return the original pattern, the type of mirror, and the line number at which the mirror is found
                        return (pattern, "H", len(fSlice))

            else:
                continue

        else:
            return (pattern, "H", 0)

def findVerticalMirror(pattern):
    """
    Find the vertical mirror of a pattern.

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
                # Split the pattern into two slices
                fSlice = rotatedPattern[:line + 1]
                sSlice = rotatedPattern[line + 1:]
                # If the start of the pattern up to the current line is the same as the end of the pattern from the next line
                if set(fSlice).issubset(sSlice):
                    # If the reverse of the second slice is the same as the first slice up to the current line
                    if fSlice[::-1] == sSlice[:len(fSlice)]:
                        # Return the original pattern, the type of mirror, and the line number at which the mirror is found
                        return (pattern, "V", len(fSlice))
                
                # If the start of the pattern up to the current line is the same as the end of the pattern from the next line
                elif set(fSlice).issuperset(sSlice):
                    # If the reverse of the second slice is the same as the first slice up to the current line
                    if sSlice == fSlice[::-1][:len(sSlice)]:
                        # Return the original pattern, the type of mirror, and the line number at which the mirror is found
                        return (pattern, "V", len(fSlice))

            else:
                continue

        else:
            return (pattern, "V", 0)

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

def patchHorizontalMirror(pattern):
    for line in range(len(pattern)):
        if line + 1 < len(pattern):
            newLine = compareLines(pattern[line], pattern[line + 1])

            if newLine:
                print(pattern[line], pattern[line + 1])

            else:
                return False

def compareLines(line1, line2):
    mismatch = 0
    for x, y in zip(line1, line2):
        if x != y:
            mismatch += 1
        
    if mismatch == 1:
        return True
    
    else:
        return False
