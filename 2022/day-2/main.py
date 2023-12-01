# https://adventofcode.com/2022/day/2
import re
from typing import List


def read_data(file_name: str = "input.txt") -> List[List[str]]:
    with open(file_name, "r") as file:
        data = file.read()

    return data.split("\n")


def main() -> int:
    data = read_data()
    val = sum(
        map(
            lambda string: int(
                re.findall(r"\b\d+\b", string)[0] + re.findall(r"\b\d+\b", string)[0]
            ),
            data,
        )
    )

    return val


if __name__ == "__main__":
    print(main())
