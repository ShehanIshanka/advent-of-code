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
        source, destination, length = row.split()
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
    for x in maps[::-1]:
        q = get_val(data[x], q)

    return q


def bin_search(left, right, output, full_dict, data, mi, print_y=False):
    a, b = left, right
    while left < right:
        mid = left + (right - left) // 2
        output[mid] = output.get(mid, full_dict.get(mid, get_loc(data, mid)))
        output[right] = output.get(right, full_dict.get(right, get_loc(data, right)))
        output[left] = output.get(left, full_dict.get(left, get_loc(data, left)))
        mi = min(output[mid], output[right], output[left], mi)

        if print_y:
            if mi == output[mid]:
                print(mi, mid)
            if mi == output[right]:
                print(mi, right)
            if mi == output[left]:
                print(mi, left)

        if output[mid] >= output[right]:
            left = mid + 1
        else:
            right = mid

    left, right = a, b
    while left < right:
        mid = left + (right - left) // 2
        output[mid] = output.get(mid, full_dict.get(mid, get_loc(data, mid)))
        output[right] = output.get(right, full_dict.get(right, get_loc(data, right)))
        output[left] = output.get(left, full_dict.get(left, get_loc(data, left)))
        mi = min(output[mid], output[right], output[left], mi)

        if print_y:
            if mi == output[mid]:
                print(mi, mid)
            if mi == output[right]:
                print(mi, right)
            if mi == output[left]:
                print(mi, left)

        if output[mid] >= output[left]:
            right = mid
        else:
            left = mid + 1

    return mi


def part2(file_name: str) -> int:
    inputs, data = read_data(file_name=file_name)
    all_vals = []
    full_dict = {}
    mi = float("inf")
    output = {}
    t = []
    for j in range(10114991):
        c = get_loc(data, j)
        for i in range(0, len(inputs), 2):
            a = inputs[i]
            b = inputs[i] + inputs[i + 1] - 1
            if a <= c <= b:
                t.append(j)
        # print(j, t)

    print(min(t))

    print(mi)
    print("---------------------------------")


if __name__ == "__main__":

    # print(part2(file_name="test.txt"))  # 30
    print(part2(file_name="input.txt"))  # 5833065
