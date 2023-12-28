# day 4 part 1
with open('day4/day4_test.txt', 'r') as f:
    lines = f.read().split('\n')

for i in lines:
   winning_nums = i.split('|')[0].rstrip(':')
   current_nums = (i.split('|')[1]).split(' ')
   print(winning_nums, current_nums)