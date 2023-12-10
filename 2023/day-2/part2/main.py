# https://adventofcode.com/2023/day/2
import math
from typing import List

possible_config = {"red": 12, "green": 13, "blue": 14}


def read_data(file_name: str = "../input.txt") -> List[str]:
    with open(file_name, "r") as file:
        data = file.read()

    games = {}
    power_sum = 0
    for d in data.split("\n"):
        power = {"red": 1, "green": 1, "blue": 1}

        game, configs = d.split(": ")
        game_id = game.split(" ")[1]

        set_list = []
        for cubes in configs.split("; "):
            sets = {}
            for cube in cubes.split(", "):
                val, colour = cube.split(" ")
                sets[colour] = int(val)
                power[colour] = max(power[colour], int(val))

            set_list.append(sets)

        power_sum += math.prod(power.values())
        games[int(game_id)] = set_list

    return power_sum


def main() -> int:
    data = read_data()
    return data


if __name__ == "__main__":
    print(main())  # 55902
