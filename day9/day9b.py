from Utilities import readFileToList
from Utilities import initialSequence
from Utilities import reduceSequence
from Utilities import solveSequenceB

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day9/day9.txt'
    # Read the input data
    lines = readFileToList(file_path)

    answer = 0

    # Go through each sequence in the input data
    for line in lines:
        sequenceMap = []
        # Convert the string into a sequence
        sequence = initialSequence(line)

        # Reduce the sequence until all numbers are 0
        while not all(num == 0 for num in sequence):
            # Append the sequence to the sequence map
            sequenceMap.append(sequence)
            # Reduce the sequence
            sequence = reduceSequence(sequence)

        sequenceMap.append(sequence)
        sequenceMap = list(reversed(sequenceMap))

        answer += solveSequenceB(sequenceMap)

    print(answer)

if __name__ == "__main__":
    main()
