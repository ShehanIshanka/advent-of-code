from typing import List


def read_segmented_data(file_name: str) -> List[List[str]]:
    with open(file_name, "r") as file:
        data = file.read()

    return [d.split("\n") for d in data.split("\n\n")]
