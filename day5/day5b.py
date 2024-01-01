from Utilities import read_file_to_list
from Utilities import extract_seeds
from Utilities import extract_map
from Utilities import get_destination
from Utilities import seed_range

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day5/day5.txt'
    seed_location = [-1, -1]
    lines = read_file_to_list(file_path)
    seeds = extract_seeds(lines[0])
    seed_to_soil = extract_map('seed-to-soil', lines)
    soil_to_fertilizer = extract_map('soil-to-fertilizer', lines)
    fertilizer_to_water = extract_map('fertilizer-to-water', lines)
    water_to_light = extract_map('water-to-light', lines)
    light_to_temperature = extract_map('light-to-temperature', lines)
    temperature_to_humidity = extract_map('temperature-to-humidity', lines)
    humidity_to_location = extract_map('humidity-to-location', lines)

    # For every seed, run this process:
    result = []
    index = 0

    for i in seeds:
        if index % 2 == 0:
            for seed in range(i, i+seeds[index+1]):
                # Find soil for the given seed
                soil = get_destination(seed, seed_to_soil)

                # Find fertilizer for the given soil
                fertilizer = get_destination(soil, soil_to_fertilizer)

                # Find water for the given fertilizer
                water = get_destination(fertilizer, fertilizer_to_water)

                # Find light for the given water
                light = get_destination(water, water_to_light)

                # Find temperature for the given light
                temperature = get_destination(light, light_to_temperature)

                # Find humidity for the given temperature
                humidity = get_destination(temperature, temperature_to_humidity)

                # Find location for the given humidity
                location = get_destination(humidity, humidity_to_location)

                # Add the location to the tuple
                if location < seed_location[1] or seed_location == [-1, -1]:
                    seed_location = (seed, location)

        index += 1

    # Print the result
    print(seed_location[1])

if __name__ == "__main__":
    main()