from Utilities import read_file_to_list
from Utilities import extract_seeds
from Utilities import extract_map
from Utilities import get_source
from Utilities import process_ranges

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day5/day5.txt'
    seed_location = [-1, -1]
    running = True
    location = -1
    lines = read_file_to_list(file_path)
    seeds = extract_seeds(lines[0])
    seed_to_soil = extract_map('seed-to-soil', lines)
    soil_to_fertilizer = extract_map('soil-to-fertilizer', lines)
    fertilizer_to_water = extract_map('fertilizer-to-water', lines)
    water_to_light = extract_map('water-to-light', lines)
    light_to_temperature = extract_map('light-to-temperature', lines)
    temperature_to_humidity = extract_map('temperature-to-humidity', lines)
    humidity_to_location = extract_map('humidity-to-location', lines)

    # Iterate through each possible location
    while running:
        location += 1
        # Get the humidity value from the location value
        humidity = get_source(location, humidity_to_location)
        # Get the temperature value from the humidity value
        temperature = get_source(humidity, temperature_to_humidity)
        # Get the light value from the temperature value
        light = get_source(temperature, light_to_temperature)
        # Get the water value from the light value
        water = get_source(light, water_to_light)
        # Get the fertilizer value from the water value
        fertilizer = get_source(water, fertilizer_to_water)
        # Get the soil value from the fertilizer value
        soil = get_source(fertilizer, soil_to_fertilizer)
        # Get the seed value from the soil value
        seed = get_source(soil, seed_to_soil)

        # Check if the seed is in the seed list
        if process_ranges(seeds, seed):
            print(location)
            running = False

if __name__ == "__main__":
    main()