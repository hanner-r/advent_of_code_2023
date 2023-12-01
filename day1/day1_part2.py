from functools import reduce

line_list = []
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        line_list.append(row)

number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

replaced_lines = []
for line in line_list:
    replace_number_line = reduce(lambda x, y: x.replace(y, number_dict[y]), number_dict, line)
    replaced_lines.append(replace_number_line)
# the problem is here - in the case of combined numbers e.g. 'twone' which is both two and one,
# the lambda function is going through the dict and replacing the 'one' part, leaving 'tw1'
# this means the 'two' is not being recognised
# same can happen for other number combos, e.g. 'oneight', 'sevenine', 'eightwo', 'nineight', 'eighthree'

new_list = []
for line in replaced_lines:
    new_line = [i for i in line if i.isnumeric()]
    new_list.append(new_line)

total = 0
for i in new_list:
    total += int(i[0] + i[-1])

print(f"Total: {total}")

# result of 53201 is too low
