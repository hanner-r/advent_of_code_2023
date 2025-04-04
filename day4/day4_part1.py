import re

with open('day4_input.txt', 'r') as input_file:
    lines = input_file.readlines()

total = 0

for line in lines:
    number_line = line.split(':')[1]
    winning_nums_str = number_line.split('|')[0]
    your_nums_str = number_line.split('|')[1]
    winning_nums = re.findall(r'(\d+)', winning_nums_str)
    your_nums = re.findall(r'(\d+)', your_nums_str)

    win_total = 0
    for num in your_nums:
        if num in winning_nums:
            win_total += 1

    card_score = 1
    if win_total == 0:
        card_score = 0
    elif win_total > 1:
        for n in range(win_total - 1):
            card_score *= 2

    total += card_score

print(f'Total: {total}')

'''Completed!'''
