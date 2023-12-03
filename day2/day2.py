def set_formatter(sets):
    sets = sets.replace(';', ',')
    sets = sets.split(', ')
    sets[0] = sets[0][len("Game " + str(game_counter) + ": "):]
    return sets

def color_and_number(x):
    for y in x.split():
        if y.isdigit():
            current_number = y
            current_number = int(current_number)

        else:
            color = y

    return color, current_number

# day 2 part 1
with open('day2/day2.txt', 'r') as f:
    lines = f.read().split('\n')

game_counter = 0
f_answer = 0

for i in lines:
    possible = True
    game_counter += 1

    sets = set_formatter(i)

    for x in sets:
        current_number = ""
        color = ""

        color, current_number = color_and_number(x)

        if color == "red" and current_number > 12:
            possible = False
        
        if color == "green" and current_number > 13:
            possible = False

        if color == "blue" and current_number > 14:
            possible = False

    if possible:
        f_answer += game_counter

print(f_answer)

# day 2 part 2
with open('day2/day2.txt', 'r') as f:
    lines = f.read().split('\n')

game_counter = 0
f_answer = 0

for i in lines:
    game_counter += 1
    min_red = 0
    min_green = 0
    min_blue = 0

    sets = set_formatter(i)

    for x in sets:
        current_number = ""
        color = ""

        color, current_number = color_and_number(x)

        if color == "red" and current_number > min_red:
            min_red = current_number

        if color == "green" and current_number > min_green:
            min_green = current_number

        if color == "blue" and current_number > min_blue:
            min_blue = current_number

    f_answer += (min_red*min_green*min_blue)

print(f_answer)