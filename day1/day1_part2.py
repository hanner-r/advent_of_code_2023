from functools import reduce

line_list = []
with open('day1_input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        line_list.append(row)

number_dict = {
    'one': 'on1e',
    'two': 'tw2o',
    'three': 'thre3e',
    'four': 'fou4r',
    'five': 'fiv5e',
    'six': 'si6x',
    'seven': 'seve7n',
    'eight': 'eigh8t',
    'nine': 'nin9e'
}

# using values of 'on1e', 'tw2o', 'thre3e' rather than '1', '2', '3' etc accounts for cases of 'overlapping' words
# e.g. now when the lambda function replaces the 'two' in 'eightwo', there is still the correct info available to
# identify the 'eight'!
# previously, replacing 'two' with '2' left 'eigh', which would not be picked up as an '8'

replaced_lines = []
for line in line_list:
    replace_number_line = reduce(lambda x, y: x.replace(y, number_dict[y]), number_dict, line)
    replaced_lines.append(replace_number_line)

new_list = []
for line in replaced_lines:
    new_line = [i for i in line if i.isnumeric()]
    new_list.append(new_line)

total = 0
for i in new_list:
    total += int(i[0] + i[-1])

print(f"Total: {total}")

''' Completed! '''
