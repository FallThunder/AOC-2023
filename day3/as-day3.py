# Day 3 Main Program
from Utilities import read_file_to_list
from Utilities import extract_next_number
from Utilities import has_special_characters

def main():
    # Path to input data
    file_path = 'AOC 2023/day3.txt'
    number_list = []

    # Convert file content to a list of strings
    lines = read_file_to_list(file_path)
    
    # Process each line
    for y, line in enumerate(lines):
        x = 0
        line = line.strip() # .strip() removes the newline character at the end of each line
    
        # Process each number in the line
        while x in range(0, len(line)):
            # Extract the next number
            number, new_x = extract_next_number(line, x)
            
            # Check if the number has any adjacent special characters in the current row
            if new_x > -1: # As long as we have not reached the end of the row
                incl = has_special_characters(lines[y].strip(), max(0,new_x - len(str(abs(number))) -1), new_x + 1) 
            
                # Check if the number has any adjacent special characters in the previous row
                if y > 0 and incl == False: # As long as this is not the first row and the number is not already marked as "include"
                    incl = has_special_characters(lines[y-1].strip(), max(0,new_x - len(str(abs(number))) -1), new_x + 1) 

                # Check if the number has any adjacent special characters in the next row
                if y < len(lines) - 1 and incl == False: # As long as this is not the last row and the number is not already marked as "include"
                    incl = has_special_characters(lines[y+1].strip(), max(0,new_x - len(str(abs(number))) -1), new_x + 1) 

            if incl == True and new_x > -1:
                number_list.append(number)

            x = new_x
    print(f'Final Sum: {sum(number_list)}')
if __name__ == "__main__":
    main()
