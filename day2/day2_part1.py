games_list = []
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        game = row[5::].strip('\n')
        games_list.append(game)

too_many = ['13 r', '14 r', '14 g', '15', '16', '17', '18', '19', '20']
valid_games = []

for game in games_list:
    cubes = game.split(':')
    if not any(x in cubes[1] for x in too_many):
        valid_games.append(game)

total = 0
for game in valid_games:
    components = game.split(':')
    total += int(components[0])

print(f'Total: {total}')

'''Completed!'''
