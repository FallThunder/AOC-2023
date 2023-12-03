# day 1 part 1
with open('day3/day3.txt', 'r') as f:
    lines = f.read().split('\n')

cur_y = 0
max_x = len(lines[0])
max_y = len(lines)
next_to_symbol = False
f_answer = 0

for y in lines:
    cur_x = 0
    current_number = ""

    for x in y:
        if x.isdigit():
            current_number += x

            for j in range(cur_x - 1, cur_x + 2):
                for k in range(cur_y - 1, cur_y + 2):
                    if k == cur_y and j == cur_x:
                        continue

                    if k < 0 or j < 0:
                        continue

                    if k >= max_y or j >= max_x:
                        continue

                    if not lines[k][j].isdigit()\
                    and lines[k][j] != ".":
                        next_to_symbol = True

        else:
            if len(current_number) > 0 and next_to_symbol:
                print(y, j, k, current_number)
                f_answer += int(current_number)
                next_to_symbol = False

            current_number = ""

        cur_x += 1
    
    if len(current_number) > 0 and next_to_symbol:
        print(y, j, k, current_number)
        f_answer += int(current_number)
        next_to_symbol = False

    cur_y += 1

print(f_answer)