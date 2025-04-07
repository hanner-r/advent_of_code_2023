"""

Steps would be...
1. Read seed number (for loop through seeds)
2. Split lines of seed-to-soil-map (lines 4-19 inc), s_to_s_line[1] is the lowest seed number for that range
3. Check if our seed number is >= s_to_s_line[1] and < (s_to_s_line[1] - s_to_s_line[2]) for each line
4. When line identified, get minimum soil number i.e. s_to_s_line[0] (if no match, seed_num = soil_num)
5. soil_num = s_to_s_line[0] + (seed_num - s_to_s_line[1])
6. Run soil_num through soil_to_fert, and so on to complete the 7 stages

"""

with open('day5_input.txt', 'r') as input_file:
    map_info = input_file.readlines()
    map_info = [line.replace('\n', '') for line in map_info]

seed_numbers = map_info[0][7:].split(' ')
seed_to_soil_map = map_info[3:19]
soil_to_fertiliser_map = map_info[21:54]
fertiliser_to_water_map = map_info[56:82]
water_to_light_map = map_info[84:122]
light_to_temperature_map = map_info[124:134]
temperature_to_humidity_map = map_info[136:173]
humidity_to_location_map = map_info[175:197]


def get_destination_num(source_num, conversion_map):
    destination_num = int(source_num)
    for line in conversion_map:
        line_items = [int(item) for item in line.split(' ')]
        if line_items[1] <= int(source_num) < line_items[1] + line_items[2]:
            destination_num = line_items[0] + (int(source_num) - line_items[1])
    return destination_num


if __name__ == '__main__':
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
    print(f'Lowest location number: {location_numbers[0]}')

'''Completed!'''
