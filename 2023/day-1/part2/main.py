# https://adventofcode.com/2023/day/1
import re
from typing import List


def read_data(file_name: str = "../input.txt") -> List[str]:
    with open(file_name, "r") as file:
        data = file.read()

    return data.split("\n")


def get_calibration(string: str) -> int:
    words_to_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pattern = rf'(?=({"|".join(words_to_digits.keys())}|\d))'
    digits = re.findall(pattern, string, flags=re.IGNORECASE)
    return int(
        words_to_digits.get(digits[0], digits[0])
        + words_to_digits.get(digits[-1], digits[-1])
    )


def main() -> int:
    data = read_data()
    return sum(map(get_calibration, data))


if __name__ == "__main__":
    print(main())  # 55902
