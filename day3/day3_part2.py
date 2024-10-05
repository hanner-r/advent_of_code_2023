import re

with open('day3_input.txt', 'r') as input_file:
    lines = [line[:-1] for line in input_file.readlines()]

total = 0
gears_dict = {}

for row, line in enumerate(lines):
    for col, idx in enumerate(line):
        if idx == '*':
            gears_dict[(row, col)] = []

for row, line in enumerate(lines):
    for num in re.finditer(r'(\d+)', line):
        for r in range(row - 1, row + 2):
            for c in range(num.start() - 1, num.end() + 1):
                if (r, c) in gears_dict:
                    gears_dict[(r, c)].append(int(num.group()))

for gear in gears_dict:
    if len(gears_dict[gear]) == 2:
        total += (gears_dict[gear][0] * gears_dict[gear][1])

print(f'Total: {total}')

'''Completed!'''
