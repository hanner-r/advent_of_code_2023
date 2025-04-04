import re

with open('day3_input.txt', 'r') as input_file:
    lines = input_file.readlines()

number_of_lines = len(lines)
line_length = len(lines[0])
symbols = '$&+=@#/*%-'
total = 0


def find_symbol(line, num_start, num_end):
    if num_start < 1:
        num_start = 1
    if num_end > 138:
        num_end = 138
    for i in range(num_start - 1, num_end + 1):
        if line[i] in symbols:
            return True


for x, line in enumerate(lines):
    nums = re.finditer(r'(\d+)', line)
    for num in nums:
        s = num.start()
        e = num.end()
        if x == 0:
            results = [find_symbol(lines[x], s, e), find_symbol(lines[x + 1], s, e)]
        elif 0 < x < 139:
            results = [find_symbol(lines[x], s, e), find_symbol(lines[x - 1], s, e), find_symbol(lines[x + 1], s, e)]
        else:
            results = [find_symbol(lines[x], s, e), find_symbol(lines[x - 1], s, e)]
        if True in results:
            total += int(num.group(1))

print(f'Total: {total}')

'''Completed!'''
