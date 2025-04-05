from day5_part1 import (get_destination_num, seed_numbers, seed_to_soil_map, soil_to_fertiliser_map,
                        fertiliser_to_water_map, water_to_light_map, light_to_temperature_map,
                        temperature_to_humidity_map, humidity_to_location_map)
"""

Steps would be...
1. Read seed number (for loop through seeds)
2. Split lines of seed-to-soil-map (lines 4-19 inc), s_to_s_line[1] is the lowest seed number for that range
3. Check if our seed number is >= s_to_s_line[1] and < (s_to_s_line[1] - s_to_s_line[2]) for each line
4. When line identified, get minimum soil number i.e. s_to_s_line[0] (if no match, seed_num = soil_num)
5. soil_num = s_to_s_line[0] + (seed_num - s_to_s_line[1])
6. Run soil_num through soil_to_fert, and so on to complete the 7 stages

"""
seed_range_dict = {}

for n in range(0, 20, 2):
    seed_range_dict[int(seed_numbers[n])] = int(seed_numbers[(n + 1)])

print(seed_range_dict)

'''
need logic here to run through each seed range in the seed_range_dict
'''

location_numbers = []
for seed_num in seed_numbers:
    soil_num = get_destination_num(seed_num, seed_to_soil_map)
    fertiliser_num = get_destination_num(soil_num, soil_to_fertiliser_map)
    water_num = get_destination_num(fertiliser_num, fertiliser_to_water_map)
    light_num = get_destination_num(water_num, water_to_light_map)
    temperature_num = get_destination_num(light_num, light_to_temperature_map)
    humidity_num = get_destination_num(temperature_num, temperature_to_humidity_map)
    location_num = get_destination_num(humidity_num, humidity_to_location_map)
    location_numbers.append(location_num)

location_numbers.sort()

# print(f'Lowest location number: {location_numbers[0]}')
