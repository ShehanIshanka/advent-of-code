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


def get_val11(d, v):
    x = v

    for i, j in d.items():
        if i[0] <= v and v <= i[1]:
            x = j[0] + v - i[0]
            break

    return x


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


def get_val2(d, v):
    for i, j in d.items():
        if i[0] <= v and v < i[1]:
            return j[0] + v - i[0]


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


def swap(my_dict):
    return dict(sorted(dict(zip(my_dict.values(), my_dict.keys())).items()))


def get_interval(d, v):
    for i, j in d.items():
        if i[0] <= v and v < i[1]:
            return i, j


def merge(a_to_b, b_to_c):
    a_to_c = {}
    # c = []
    # for i in a_to_b.copy():
    #     if i[0] == i[1]:
    #         c.append(i[0])
    #
    # for i in b_to_c.copy():
    #     if i[0] == i[1]:
    #         c.append(i[0])

    a_keys_list = [item for sublist in a_to_b.keys() for item in sublist]
    b_keys_list = [item for sublist in b_to_c.keys() for item in sublist]
    # a_keys_list.remove(0)
    # a_keys_list.remove(float("inf"))

    a_values_list = [item for sublist in a_to_b.values() for item in sublist]
    b_values_list = [item for sublist in b_to_c.values() for item in sublist]
    # if 0 in a_values_list:
    #     a_values_list.remove(0)
    # if float("inf") in a_values_list:
    #     a_values_list.remove(float("inf"))
    # full_list = list(set(a_keys_list + b_keys_list))
    # full_list = sorted(full_list+ list(set(c)))
    # if len(full_list) % 2 != 0:
    #     full_list[-2:] = [full_list[-2], full_list[-2] + 1, full_list[-1]]
    full_list = sorted(a_keys_list + b_keys_list + a_values_list + b_values_list)

    for i in range(0, len(full_list) - 1):
        a, b = full_list[i], full_list[i + 1]
        a_to_c[(a, b)] = (
            get_val(b_to_c, get_val(a_to_b, a)),
            get_val(b_to_c, get_val(a_to_b, b)),
        )
    # print(a_to_b)
    # print(b_to_c)
    # print(a_to_c)
    # print("---------:;;;;;;;;")
    return dict(sorted(a_to_c.items()))


def part1(file_name: str) -> int:
    inputs, data = read_data(file_name=file_name)

    m = []

    for i in inputs:
        y = i
        for x in maps:
            # print(y, x, data[x])
            y = get_val(data[x], y)
            # print(y)

        m.append(y)

    print(m)
    print(min(m))


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
        all_vals.extend(data[i].keys())
        all_vals.extend(data[i].values())

    full_list = sorted(list(set(all_vals)))
    print(full_list)
    mi = float("inf")
    for i in range(0, len(inputs), 2):
        s = get_loc(data, inputs[i])
        e = get_loc(data, inputs[i] + inputs[i + 1] - 1)

        a = inputs[i]
        b = inputs[i] + inputs[i + 1] - 1

        mi = min(s, e, mi)
        for j in full_list:
            # print(j)
            if j[1] < a:
                continue

            if b < j[0]:
                break

            if j[0] <= a <= j[1] <= b:
                t = get_loc(data, j[1])
                if s != t:
                    r = min(range(min(s, t), max(s, t)))
                    mi = min(mi, r)

            if a <= j[0] <= b <= j[1]:
                t = get_loc(data, j[0])
                if e != t:
                    r = min(range(min(t, e), max(t, e)))
                    mi = min(mi, r)

    # for i in range(0, len(inputs), 2):
    #     s = get_val(d, inputs[i])
    #     e = get_val(d, inputs[i] + inputs[i + 1] - 1)
    #     # print(s,inputs[i])
    #     m[(inputs[i], inputs[i] + inputs[i + 1] - 1)] = (s, e)
    #
    # print(m)
    print(mi)
    print("---------------------------------")


if __name__ == "__main__":
    # print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667

    print(part2(file_name="test.txt"))  # 30
    print(part2(file_name="input.txt"))  # 5833065
