# https://adventofcode.com/2022/day/1
from common.utils import read_segmented_data


def main() -> int:
    data = read_segmented_data(file_name="input.txt")
    integer_list_of_list = map(lambda inner_list: list(map(int, inner_list)), data)

    return max(map(sum, integer_list_of_list))


if __name__ == "__main__":
    print(main())
