line_list = []
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        line_list.append(row)

new_list = []
for line in line_list:
    new_line = [i for i in line if i.isnumeric()]
    new_list.append(new_line)

total = 0
for i in new_list:
    total += int(i[0] + i[-1])

print(f"Total: {total}")

''' Completed! '''
