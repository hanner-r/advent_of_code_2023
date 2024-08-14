import re

with open('day3_input.txt', 'r') as input_file:
    lines = [line[:-1] for line in input_file.readlines()]

number_of_lines = len(lines)
line_length = len(lines[0])
total = 0
gears = []

for x, line in enumerate(lines):
    for y, idx in enumerate(line):
        if idx == '*':
            gears.append((x, y))
            nums = re.finditer(r'(\d+)', line)

# idk !!!!
# for gear in gears:
#     x = gear[0]
#     y = gear[1]
#     for x in range(x+1, x-1):
#         for y in range(y+1, y-1):
#             nums = re.finditer(r'(\d+)', lines[x][y])

print(f'Total: {total}')
