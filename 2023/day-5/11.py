# https://adventofcode.com/2023/day/5
from typing import Dict, List, Set


def get_val(d, v):
    x = v
    for i, j in d.items():
        if i <= v and v < i + j[0]:
            x = j[1] + v - i
            break
    # print(x)
    return x


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    splits = data.split("\n")
    i = 0
    inputs = []
    seed_to_soil_map = {}
    soil_to_fertilizer_map = {}
    fertilizer_to_water_map = {}
    water_to_light_map = {}
    light_to_temperature_map = {}
    temperature_to_humidity_map = {}
    humidity_to_location_map = {}

    while i < len(splits):
        row = splits[i]

        if i == 0:
            inputs.extend(list(map(int, row.split(": ")[1].split())))
        elif row == "seed-to-soil map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            seed_to_soil_map = d
        elif row == "soil-to-fertilizer map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            soil_to_fertilizer_map = d
        elif row == "fertilizer-to-water map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            fertilizer_to_water_map = d
        elif row == "water-to-light map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            water_to_light_map = d
        elif row == "light-to-temperature map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            light_to_temperature_map = d
        elif row == "temperature-to-humidity map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            temperature_to_humidity_map = d
        elif row == "humidity-to-location map:":
            d = {}
            while row.strip() != "":
                i = i + 1
                row = splits[i]
                if row == "":
                    break
                destination, source, length = row.split()
                d[int(source)] = (int(length), int(destination))
            humidity_to_location_map = d

        i = i + 1

    m = []
    for i in inputs:

        x = i
        x = get_val(seed_to_soil_map, x)
        x = get_val(soil_to_fertilizer_map, x)
        x = get_val(fertilizer_to_water_map, x)
        x = get_val(water_to_light_map, x)
        x = get_val(light_to_temperature_map, x)
        x = get_val(temperature_to_humidity_map, x)
        x = get_val(humidity_to_location_map, x)

        m.append(x)

    print(min(m))


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)


def part2(file_name: str) -> int:
    pass


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
