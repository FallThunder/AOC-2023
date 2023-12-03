# day 1 part 1
with open('day1/day1.txt', 'r') as f:
    lines = f.read().split('\n')

digits_in_string = []
final_answer = 0

for i in lines:
    for x in i:
        if x.isdigit():
            digits_in_string.append(x)

    final_answer += int(digits_in_string[0] + digits_in_string[-1])
    digits_in_string = []

print(final_answer)

# day 1 part 2
with open('day1/day1.txt', 'r') as f:
    lines = f.read().split('\n')

digit_to_char = {
    'zero': '0', 'one': '1',
    'two': '2', 'three': '3',
    'four': '4', 'five':'5',
    'six': '6', 'seven': '7',
    'eight': '8', 'nine': '9'
}
digits_in_string = []
char_string = ""
final_answer = 0

for i in lines:
    for x in i:
        if x.isdigit():
            char_string = ""
            digits_in_string.append(x)

        else:
            char_string += x
            print(char_string)

            for l in digit_to_char:
                if l in char_string:
                    digits_in_string.append(digit_to_char[l])
                    print(l + " found")
                    char_string = char_string[-1]

    print(digits_in_string, digits_in_string[0], digits_in_string[-1])
    final_answer += int(digits_in_string[0] + digits_in_string[-1])
    digits_in_string = []
    char_string = ""

print(final_answer)