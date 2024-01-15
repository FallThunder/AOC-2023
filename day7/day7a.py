from Utilities import read_file_to_list
from Utilities import hand_type

def main():
    list = []
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day7/day7.txt'
    # Read the input data
    lines = read_file_to_list(file_path)
    # Find the hand type
    for hand in lines:
        list.append(hand_type(hand))
    # Sort the list by 2nd element in tuple in ascending order
    list.sort(key=lambda x: x[2], reverse=False)
    # Multiply the bid with the index + 1 of the hand and sum them up
    sum = 0
    for i in range(len(list)):
        sum += int(list[i][1]) * (i + 1)

    print(sum)

if __name__ == "__main__":
    main()