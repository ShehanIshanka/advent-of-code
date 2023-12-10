# https://adventofcode.com/2023/day/5
from typing import Dict, List, Set

maps = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]


def get_val(d, v):
    x = v
    for i, j in d.items():
        if i[0] == v:
            x = j[0]
            break
        if i[1] == v:
            x = j[1]
            break

        if i[0] < v < i[1]:
            x = j[0] + v - i[0]
            break

    return x


def read_map(splits, start):
    d = {}
    mi, ma = float("inf"), 0
    row = splits[start]
    while row.strip() != "":
        start = start + 1
        row = splits[start]
        if row == "":
            break
        destination, source, length = row.split()
        d[(int(source), int(source) + int(length) - 1)] = (
            int(destination),
            int(destination) + int(length) - 1,
        )
        mi = min(mi, int(source))
        ma = max(ma, int(source) + int(length) - 1)

    if mi != 0:
        d[(0, mi - 1)] = (get_val(d, 0), get_val(d, mi - 1))

    d[(ma + 1, float("inf"))] = (get_val(d, ma + 1), get_val(d, float("inf")))

    return dict(sorted(d.items())), start


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    splits = data.split("\n")
    i = 0
    inputs = []
    data_map = {}

    while i < len(splits):
        row = splits[i]

        if i == 0:
            inputs.extend(list(map(int, row.split(": ")[1].split())))
        elif row in maps:
            data_map[row], i = read_map(splits, i)

        i = i + 1

    return inputs, data_map


def get_loc(data, q):
    i = 0
    for x in maps:
        q = get_val(data[x], q)
        if i == 8:
            break
        i = i + 1

    return q


def part2(file_name: str) -> int:
    inputs, data = read_data(file_name=file_name)
    all_vals = []
    for i in maps:
        all_vals.extend([item for sublist in data[i].keys() for item in sublist])
        all_vals.extend([item for sublist in data[i].values() for item in sublist])

    full_list = sorted(list(set(all_vals)))
    full_dict = {x: get_loc(data, x) for x in full_list}
    mi = float("inf")
    print(full_dict)

    output = {}
    mx = float("inf")
    p, q = inputs[0], inputs[1]
    for i in range(0, len(inputs), 2):
        a = inputs[i]
        b = inputs[i] + inputs[i + 1] - 1

        s = output[a] = output.get(a, full_dict.get(a, get_loc(data, a)))
        e = output[b] = output.get(b, full_dict.get(b, get_loc(data, b)))

        mx = min(mx, s, e)

        if mx == s or mx == e:
            p, q = inputs[i], inputs[i + 1]

    inputs = [p, q]
    print(inputs)

    for i in range(0, len(inputs), 2):
        a = inputs[i]
        b = inputs[i] + inputs[i + 1] - 1

        s = output[a] = output.get(a, full_dict.get(a, get_loc(data, a)))
        e = output[b] = output.get(b, full_dict.get(b, get_loc(data, b)))

        mi = min(s, e, mi)

        for j, k in full_dict.items():
            output[j] = k
            if j < a:
                continue

            if b < j:
                break

            if a <= j <= b:
                mi = min(mi, k)
                if s > k and e > k:
                    if s > e:
                        for g in range(a, j):
                            r = output[g] = output.get(
                                g, full_dict.get(g, get_loc(data, g))
                            )
                            mi = min(mi, r)
                    if e > s:
                        for g in range(j, b):
                            r = output[g] = output.get(
                                g, full_dict.get(g, get_loc(data, g))
                            )
                            mi = min(mi, r)

    print(mi)
    print("---------------------------------")


if __name__ == "__main__":

    print(part2(file_name="test.txt"))  # 30
    print(part2(file_name="input.txt"))  # 5833065
