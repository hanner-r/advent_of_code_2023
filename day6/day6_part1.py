import re

with open('day6_input.txt', 'r') as input_file:
    times_and_distances = input_file.readlines()
    times = re.findall(r'\d+', times_and_distances[0])
    distances = re.findall(r'\d+', times_and_distances[1])


def count_winning_options(time, distance):
    wins = 0
    for x in range(time):
        race_distance = x * (time - x)
        if race_distance > distance:
            wins += 1
    return wins


if __name__ == '__main__':
    totals = 1
    for n in range(len(times)):
        totals *= count_winning_options(int(times[n]), int(distances[n]))

    print(f'Product of win totals: {totals}')

'''Completed!'''
