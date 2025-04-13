from day6_part1 import count_winning_options, times, distances

time = int(times[0] + times[1] + times[2] + times[3])
distance = int(distances[0] + distances[1] + distances[2] + distances[3])

print(f'Total winning options: {count_winning_options(time, distance)}')

'''Completed!'''
'''test'''