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


def get_val_min(d, v):
    # d[int(source)] = (int(length), int(destination))
    l, m = [], []
    for i, j in d.items():
        l.append()
        m.append()

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

    def get_loc(x):
        x = get_val(seed_to_soil_map, x)
        x = get_val(soil_to_fertilizer_map, x)
        x = get_val(fertilizer_to_water_map, x)
        x = get_val(water_to_light_map, x)
        x = get_val(light_to_temperature_map, x)
        x = get_val(temperature_to_humidity_map, x)
        return get_val(humidity_to_location_map, x)

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

    m, n = [], []
    i = 0
    while i < len(inputs):
        for c in [inputs[i], inputs[i] + inputs[i + 1] - 1]:
            x = c
            x = get_val(seed_to_soil_map, x)
            x = get_val(soil_to_fertilizer_map, x)
            x = get_val(fertilizer_to_water_map, x)
            x = get_val(water_to_light_map, x)
            x = get_val(light_to_temperature_map, x)
            x = get_val(temperature_to_humidity_map, x)
            x = get_val(humidity_to_location_map, x)
            n.append(c)
            m.append(x)

        i = i + 2

    b = min(m)
    c = m.index(b)
    # print(c)
    print(n[c - 1], n[c], "----", m[c - 1], m[c])

    p, q = [], []
    s = False
    for i, j in seed_to_soil_map.items():
        if n[c - 1] <= i < n[c]:
            x, s = i, True

        elif n[c - 1] <= i + j[0] < n[c]:
            x, s = i + j[0], True

        elif i <= n[c - 1] < i + j[0]:
            x, s = i + j[0], True

        elif i <= n[c] < i + j[0]:
            x, s = i + j[0], True

        if s:
            q.append(x)
            p.append(get_loc(x))
            s = False

    print(p)
    print(q)
    print(get_loc(82))

    # p = []
    # for l in range(n[c-1],n[c]):
    #     x = l
    #     x = get_val(seed_to_soil_map, x)
    #     x = get_val(soil_to_fertilizer_map, x)
    #     x = get_val(fertilizer_to_water_map, x)
    #     x = get_val(water_to_light_map, x)
    #     x = get_val(light_to_temperature_map, x)
    #     x = get_val(temperature_to_humidity_map, x)
    #     x = get_val(humidity_to_location_map, x)
    #     p.append(x)
    #     # if min(p) == x:
    #     #     break
    # print(p)
    # print(min(p))

    print("qqqqq")


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)


def part2(file_name: str) -> int:
    pass


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
