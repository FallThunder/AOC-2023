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

def find_matches(current, winners, final):
    matches = 0

    for x in current:
        if x in winners:
            matches += 1

    if matches == 1:
       final += 1

    elif matches > 1:
        final += 2**(matches-1)
    
    return final, matches

# # day 4 part 1
# with open('day4/day4.txt', 'r') as f:
#     lines = f.read().split('\n')

# card = 1
# final = 0

# for i in lines:
#     winners = extract_winners(i, card)
#     current = extract_current(i)
#     final = find_matches(current, winners, final)[0]

#     card += 1

# print(final)

# day 4 part 2
with open('day4/day4_test.txt', 'r') as f:
    lines = f.read().split('\n')

card_count = {x:1 for x in lines}
card = 1

for i in card_count:
    card_iter = list(card_count).index(i)
    final = 0

    winners = extract_winners(i, card)
    current = extract_current(i)
    final = find_matches(current, winners, final)[0]

    for n in range(1, final + 1):
        for l in card_count:
            if list(card_count).index(l) > card_iter:
                card_count[l] += 1*card_count[i]

    card += 1
    print(card_count)
    print(sum(card_count[z] for z in card_count), "\n")

print(sum(card_count[z] for z in card_count))