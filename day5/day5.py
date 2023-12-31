from Utilities import read_file_to_list
from Utilities import extract_seeds
from Utilities import extract_map
from Utilities import get_destination

def main():
    # Path to input data
    file_path = '/Users/pratyushsiva/VSCode/AOC 2023/day5/day5.txt'
    seed_location = []
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
    for seed in seeds:
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
        seed_location.append((seed, location))

    # Print the result
    print(min(seed_location, key=lambda x: x[1])[1])

    

if __name__ == "__main__":
    main()