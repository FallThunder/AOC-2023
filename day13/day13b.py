from Utilities import readFileToList
from Utilities import extractPatterns
from Utilities import patchHorizontalMirror
from Utilities import findHorizontalMirror
from Utilities import findVerticalMirror
from Utilities import scorePattern

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day13/day13_test.txt'
    # Read the input data
    lines = readFileToList(file_path)
    # Extract patterns from the input data
    patterns = extractPatterns(lines)
    # Create a variable to store the final score
    final = 0
    # For each pattern in the list of patterns
    for pattern in patterns:
        pattern = patchHorizontalMirror(pattern)
    #     # Find the horizontal mirror of the pattern
    #     patternData = findHorizontalMirror(pattern)
    #     # If the mirror is not found
    #     if patternData[2] == 0:
    #         # Find the vertical mirror of the pattern
    #         patternData = findVerticalMirror(pattern)

    #     if patternData[2] == 0:
    #         for i in patternData[0]:
    #             print(i)

    #         print()

    #     # Add the score of the pattern to the final score
    #     final += scorePattern(patternData)

    # print(final)

if __name__ == "__main__":
    main()
