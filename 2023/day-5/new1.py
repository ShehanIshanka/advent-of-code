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

    return q


def part2(file_name: str) -> int:
    inputs, data = read_data(file_name=file_name)
    all_vals = []
    full_dict = {}
    mi = float("inf")

    # for i in maps:
    #     all_vals.extend([item for sublist in data[i].keys() for item in sublist])
    #     all_vals.extend([item for sublist in data[i].values() for item in sublist])
    #
    # full_list = sorted(list(set(all_vals)))
    # full_dict = {x: get_loc(data, x) for x in full_list}
    # mi = float("inf")
    # print(full_dict)

    output = {}

    left, right = 3055971715, 3109084187
    while left < right:
        mid = left + (right - left) // 2
        output[mid] = output.get(mid, full_dict.get(mid, get_loc(data, mid)))
        output[right] = output.get(right, full_dict.get(right, get_loc(data, right)))
        output[left] = output.get(left, full_dict.get(left, get_loc(data, left)))
        mi = min(output[mid], output[right], output[left], mi)

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

    left, right = 3055971715, 3109084187
    while left < right:
        mid = left + (right - left) // 2
        output[mid] = output.get(mid, full_dict.get(mid, get_loc(data, mid)))
        output[right] = output.get(right, full_dict.get(right, get_loc(data, right)))
        output[left] = output.get(left, full_dict.get(left, get_loc(data, left)))

        mi = min(output[mid], output[right], output[left], mi)
        if output[mid] >= output[right]:
            left = mid + 1
        else:
            right = mid

    print(mi)
    print("0000000000000000000000000000")
    print(get_loc(data, 3099986030))
    print(get_loc(data, 3099986031))
    print(get_loc(data, 3099986032))
    print("0000000000000000000000000000")

    for i in range(0, len(inputs), 2):
        a = inputs[i]
        b = inputs[i] + inputs[i + 1] - 1

        s = output[a] = output.get(a, full_dict.get(a, get_loc(data, a)))
        e = output[b] = output.get(b, full_dict.get(b, get_loc(data, b)))

        if a <= 3099986031 <= b:
            print("TRUEEEEEEEEEEEEEEEEEEEEE")

        # print(get_loc(data, 3055971715))
        # print(get_loc(data, 3055971716))
        # if a <= 3109084187 <= b:
        #     print("aaaa", a, i, b, "|", s, get_loc(data, 3109084186), e)
        #     print("aaaa", a, i, b, "|", s, get_loc(data, 3109084187), e)
        #     print("aaaa", a, i, b, "|", s, get_loc(data, 3109084188), e)
        #     c = 3055786218
        #     while True:
        #         r = min(mi, get_loc(data, c))
        #         c = c + 1
        #         if mi < r or c < a:
        #             break
        #         print(c, r)
        #
        #         mi = min(r, mi)

        mi = min(s, e, mi)

        left, right = a, b
        while left < right:
            mid = left + (right - left) // 2
            output[mid] = output.get(mid, full_dict.get(mid, get_loc(data, mid)))
            output[right] = output.get(
                right, full_dict.get(right, get_loc(data, right))
            )
            output[left] = output.get(left, full_dict.get(left, get_loc(data, left)))

            mi = min(output[mid], output[right], output[left], mi)
            if output[mid] >= output[right]:
                left = mid + 1
            else:
                right = mid

        for n in range(min(left, right), max(left, right)):
            r = output[n] = output.get(n, full_dict.get(n, get_loc(data, n)))
            mi = min(s, r)

        left, right = a, b
        while left < right:
            mid = left + (right - left) // 2
            output[mid] = output.get(mid, full_dict.get(mid, get_loc(data, mid)))
            output[right] = output.get(
                right, full_dict.get(right, get_loc(data, right))
            )
            output[left] = output.get(left, full_dict.get(left, get_loc(data, left)))

            mi = min(output[mid], output[right], output[left], mi)
            if mi == output[mid]:
                print(mi, mid)
            if mi == output[right]:
                print(mi, right)
            if mi == output[left]:
                print(mi, left)
            if output[mid] >= output[right]:
                right = mid
            else:
                left = mid + 1

        for n in range(min(left, right), max(left, right)):
            r = output[n] = output.get(n, full_dict.get(n, get_loc(data, n)))
            mi = min(s, r)

    print(mi)
    print("---------------------------------")


if __name__ == "__main__":

    print(part2(file_name="test.txt"))  # 30
    print(part2(file_name="input.txt"))  # 5833065
