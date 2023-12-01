# https://adventofcode.com/2023/day/1
import re
from typing import List


def read_data(file_name: str = "../input.txt") -> List[str]:
    with open(file_name, "r") as file:
        data = file.read()

    return data.split("\n")


def get_calibration(string: str) -> int:
    digits = re.findall(r"\d", string)
    return int(digits[0] + digits[-1])


def main() -> int:
    data = read_data()
    return sum(map(get_calibration, data))


if __name__ == "__main__":
    print(main())  # 56465
