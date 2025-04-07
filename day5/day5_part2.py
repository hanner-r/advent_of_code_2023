from day5_part1 import (seed_numbers, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map,
                        water_to_light_map, light_to_temperature_map, temperature_to_humidity_map,
                        humidity_to_location_map)

"""

1. run through every location number possible from 0 up
2. backwards mapping through all the steps - get a seed number
3. check if seed number is valid, i.e. sits in one of the seed number ranges given

"""

seed_range_dict = {}

for n in range(0, 20, 2):
    seed_range_dict[int(seed_numbers[n])] = int(seed_numbers[(n + 1)])


def get_source_num(destination_num, conversion_map):
    source_num = int(destination_num)
    for line in conversion_map:
        line_items = [int(item) for item in line.split(' ')]
        if line_items[0] <= int(destination_num) < line_items[0] + line_items[2]:
            source_num = line_items[1] + (int(destination_num) - line_items[0])
            return source_num
    return source_num


def check_valid_seed_num(seed_number):
    # need logic here to check the number found against the given seed number ranges
    for key in seed_range_dict.keys():
        if key <= seed_number < (key + seed_range_dict[key]):
            return True
    return False


location_found = False
location_num = 0

if __name__ == '__main__':
    while not location_found:

        humidity_num = get_source_num(location_num, humidity_to_location_map)
        temperature_num = get_source_num(humidity_num, temperature_to_humidity_map)
        light_num = get_source_num(temperature_num, light_to_temperature_map)
        water_num = get_source_num(light_num, water_to_light_map)
        fertiliser_num = get_source_num(water_num, fertiliser_to_water_map)
        soil_num = get_source_num(fertiliser_num, soil_to_fertiliser_map)
        seed_num = get_source_num(soil_num, seed_to_soil_map)

        location_found = check_valid_seed_num(seed_num)
        if location_found:
            print(f'Lowest location number: {location_num}')
        else:
            location_num += 1

'''Takes nearly 2 minutes to run, but - Completed!!'''
