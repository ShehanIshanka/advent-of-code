# https://adventofcode.com/2023/day/2
from typing import List

possible_config = {"red": 12, "green": 13, "blue": 14}


def read_data(file_name: str = "../input.txt") -> List[str]:
    with open(file_name, "r") as file:
        data = file.read()

    games = {}
    id_sum = 0
    for d in data.split("\n"):
        game, configs = d.split(": ")
        game_id = game.split(" ")[1]

        set_list = []
        f = True
        for cubes in configs.split("; "):
            sets = {}
            for cube in cubes.split(", "):
                val, colour = cube.split(" ")
                sets[colour] = int(val)
                if possible_config[colour] < int(val):
                    f = False
                    break

            if not f:
                break

        else:
            id_sum += int(game_id)

            set_list.append(sets)

        games[int(game_id)] = set_list

    return id_sum


def main() -> int:
    data = read_data()
    return data


if __name__ == "__main__":
    print(main())  # 55902
