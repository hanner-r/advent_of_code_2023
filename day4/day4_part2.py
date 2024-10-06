import re

with open('day4_input.txt', 'r') as input_file:
    lines = input_file.readlines()

total_list = []


def check_wins(lines_list, line_number):
    total_list.append('')
    line = lines_list[line_number]

    number_line = line.split(':')[1]
    winning_nums_str = number_line.split('|')[0]
    your_nums_str = number_line.split('|')[1]
    winning_nums = re.findall(r'(\d+)', winning_nums_str)
    your_nums = re.findall(r'(\d+)', your_nums_str)

    win_total = 0

    for num in your_nums:
        if num in winning_nums:
            win_total += 1
    if win_total > 0:
        for n in range(1, win_total + 1):
            check_wins(lines_list, line_number + n)


for x, each_line in enumerate(lines):
    check_wins(lines, x)

total = (len(total_list))

print(f'Total: {total}')

'''Completed! But there is a better way...this one takes a long time to run.'''
