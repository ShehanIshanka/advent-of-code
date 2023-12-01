# https://adventofcode.com/2022/day/1
from typing import List


def read_segmented_data(file_name: str) -> List[List[str]]:
    with open(file_name, "r") as file:
        data = file.read()

    return [d.split("\n") for d in data.split("\n\n")]


def main() -> int:
    data = read_segmented_data(file_name="input.txt")
    integer_list_of_list = map(lambda inner_list: list(map(int, inner_list)), data)

    return max(map(sum, integer_list_of_list))


if __name__ == "__main__":
    print(main())
