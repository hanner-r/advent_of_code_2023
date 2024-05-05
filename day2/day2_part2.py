import re

games_list = []
with open('day2_input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        game = row[8::].strip('\n')
        games_list.append(game)

total = 0
for game in games_list:
    reds = re.findall(r'\d* r', game)
    min_red = max([int(red[0:-2]) for red in reds])

    greens = re.findall(r'\d* g', game)
    min_green = max([int(green[0:-2]) for green in greens])

    blues = re.findall(r'\d* b', game)
    min_blue = max([int(blue[0:-2]) for blue in blues])

    game_total = min_red * min_green * min_blue
    total += game_total

print(f'Total: {total}')

'''Completed!'''
