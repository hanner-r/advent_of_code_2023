with open('thing.txt', 'r') as input_file:
    lines = input_file.DictReader(input_file)
    for row in lines:
        list.append(row)