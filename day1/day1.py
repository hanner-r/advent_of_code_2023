line_list = []
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        line_list.append(row)
print(line_list)