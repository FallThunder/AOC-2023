def extract_winners(sheet, card_num):
    winning_nums = sheet.split('|')[0].replace\
    ("Card {}: ".format(card_num), "").split(' ')
    for i in winning_nums:
       if i == '' or i == ' ':
           winning_nums.remove(i)

    return winning_nums

def extract_current(sheet):
    current_nums = sheet.split('|')[1].split(' ')
    for i in current_nums:
       if i == '' or i == ' ':
           current_nums.remove(i)

    return current_nums

# day 4 part 1
with open('day4/day4.txt', 'r') as f:
    lines = f.read().split('\n')

card = 1
final = 0

for i in lines:
    matches = 0
    winners = extract_winners(i, card)
    current = extract_current(i)

    for x in current:
        if x in winners:
            matches += 1

    if matches == 1:
       final += 1

    elif matches > 1:
        final += 2**(matches-1)

    else:
        continue

    card += 1

print(final)

# day 4 part 2
with open('day4/day4_test.txt', 'r') as f:
    lines = f.read().split('\n')

card = 1
final = 0

for i in lines:
    matches = 0
    winners = extract_winners(i, card)
    current = extract_current(i)

    for x in current:
        if x in winners:
            matches += 1

    if matches == 1:
       final += 1

    elif matches > 1:
        final += 2**(matches-1)

    else:
        continue

    card += 1

print(final)