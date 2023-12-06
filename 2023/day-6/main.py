# https://adventofcode.com/2023/day/6
from typing import Dict, Tuple
from functools import reduce


def read_data_part1(file_name: str) -> Dict[int, int]:
    with open(file_name, "r") as file:
        data = file.read().split("\n")

    times = data[0].split(":")[1].strip().split()
    distances = data[1].split(":")[1].strip().split()
    records = {}

    for i in range(len(times)):
        records[int(times[i])] = int(distances[i])

    return records


def read_data_part2(file_name: str) -> Tuple[int, int]:
    with open(file_name, "r") as file:
        data = file.read().split("\n")

    time = int("".join(data[0].split(":")[1].strip().split()))
    distance = int("".join(data[1].split(":")[1].strip().split()))

    return time, distance


def part1(file_name: str) -> int:
    data = read_data_part1(file_name=file_name)

    winning_ways = map(
        lambda item: sum([1 for t in range(1, item[0]) if (item[0] - t) * t > item[1]]),
        data.items(),
    )
    return reduce(lambda x, y: x * y, winning_ways)


def part2(file_name: str) -> int:
    time, dist = read_data_part2(file_name=file_name)
    return sum([1 for t in range(1, time) if (time - t) * t > dist])


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 288
    print(part1(file_name="input.txt"))  # 170000

    print(part2(file_name="test.txt"))  # 71503
    print(part2(file_name="input.txt"))  # 20537782
