games_list = []
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for row in lines:
        game = row[8::].strip('\n')
        games_list.append(game)

print(games_list)
for game in games_list:
    turns = game.split(';')
