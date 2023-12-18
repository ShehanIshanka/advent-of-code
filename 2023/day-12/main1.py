# https://adventofcode.com/2023/day/12
from typing import Dict, List, Set
import re
from itertools import product


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards, coms, coms_str = [], [], []
    for row in data.split("\n"):
        a, b = row.split()
        cards.append(a)
        coms.append(list(map(int, b.split(","))))
        coms_str.append(b.split(","))

    return cards, coms, coms_str


def get_all_combinations(symbols, length):
    return ["".join(i) for i in list(product(symbols, repeat=length))]


def part1(file_name: str) -> int:
    data, com, coms_str = read_data(file_name=file_name)
    v1 = get_all_combinations(["#", "."], 4)
    c = 0
    for i in range(len(data)):
        # t = re.sub(r"\.{2,}", ".", data[i])
        t = data[i]
        T = "{}".join([t] * 5)
        b = t.count("?")
        # t ? t ? t ? t ? t
        # t ? | t | ? t ? | t |? t
        #
        d = 0
        y = {}
        al = get_all_combinations(["#", "."], b)
        cv = coms_str[i] * 2
        az = {",".join(cv[:j]): 1 for j in range(len(cv) + 1)}

        for u in al:
            r = re.sub(r"\.{2,}", ".", t.replace("?", "{}").format(*u))
            p = ",".join([str(z.count("#")) for z in r.split(".") if "#" in z])
            y[p] = y.get(p, 0) + az.get(p, 0)
            p = ",".join([str(z.count("#")) for z in (r + "#").split(".") if "#" in z])
            y[p] = y.get(p, 0) + az.get(p, 0)
            p = ",".join([str(z.count("#")) for z in ("#" + r).split(".") if "#" in z])
            y[p] = y.get(p, 0) + az.get(p, 0)

        pr = list(product(az.keys(), repeat=5))
        print(y)
        # for a1, a2, a3, a4, a5 in pr:
        #     h = y.get(a1, 0) * y.get(a2, 0) * y.get(a3, 0) * y.get(a4, 0) * y.get(a5, 0)
        #     if h == 0:
        #         continue
        #     u = []
        #     u.append(".".join(["#" * int(st) for st in a1.split(",") if st.isdigit()]))
        #     u.append(".".join(["#" * int(st) for st in a2.split(",") if st.isdigit()]))
        #     u.append(".".join(["#" * int(st) for st in a3.split(",") if st.isdigit()]))
        #     u.append(".".join(["#" * int(st) for st in a4.split(",") if st.isdigit()]))
        #     u.append(".".join(["#" * int(st) for st in a5.split(",") if st.isdigit()]))
        #     w = "{}".join(u)
        #     for v in v1:
        #         w1 = re.sub(r"\.{2,}", ".", w.format(*v))
        #
        #         if com[i] * 5 == [z.count("#") for z in w1.split(".") if "#" in z]:
        #             print(a1, a2, a3, a4, a5, h)
        #             if h > 0:
        #                 d = d + h
        #             else:
        #                 d = d + 1

        for a1, a2, a3, a4, a5 in pr:
            h = y.get(a1, 0) * y.get(a2, 0) * y.get(a3, 0) * y.get(a4, 0) * y.get(a5, 0)
            if h == 0:
                continue
            u = []
            u.append(".".join(["#" * int(st) for st in a1.split(",") if st.isdigit()]))
            u.append(".".join(["#" * int(st) for st in a2.split(",") if st.isdigit()]))
            u.append(".".join(["#" * int(st) for st in a3.split(",") if st.isdigit()]))
            u.append(".".join(["#" * int(st) for st in a4.split(",") if st.isdigit()]))
            u.append(".".join(["#" * int(st) for st in a5.split(",") if st.isdigit()]))
            w = ".".join(u)

            if com[i] * 5 == [z.count("#") for z in w.split(".") if "#" in z]:
                if h > 0:
                    d = d + h
                else:
                    d = d + 1

        # print(pr)
        # print(y)
        # for u in get_all_combinations(["#", "."], b):
        #     replaced_string = t.replace("?", "{}")
        #     r = re.sub(r"\.{2,}", ".", replaced_string.format(*u))
        #     # print(com[i], r, [z.count("#") for z in r.split(".") if "#" in z])
        #     # y.l()
        #     if com[i] == [z.count("#") for z in r.split(".") if "#" in z]:
        #         y.append(u)
        #
        # w1 = len(y)
        #
        # if t[-1] == ".":
        #     t = "?" + t
        #     y = []
        #     for u in get_all_combinations(["#", "."], b+1):
        #         replaced_string = t.replace("?", "{}")
        #         r = re.sub(r"\.{2,}", ".", replaced_string.format(*u))
        #         # print(com[i], r, [z.count("#") for z in r.split(".") if "#" in z])
        #         # y.l()
        #         if com[i] == [z.count("#") for z in r.split(".") if "#" in z]:
        #             y.append(u)
        #
        #     w2 = len(y)
        # else:
        #     t =  t + "?"
        #     y = []
        #     for u in get_all_combinations(["#", "."], b+1):
        #         replaced_string = t.replace("?", "{}")
        #         r = re.sub(r"\.{2,}", ".", replaced_string.format(*u))
        #         # print(com[i], r, [z.count("#") for z in r.split(".") if "#" in z])
        #         # y.l()
        #         if com[i] == [z.count("#") for z in r.split(".") if "#" in z]:
        #             y.append(u)
        #
        #     w2 = len(y)
        #
        # w = w1*(w2**4)
        # print(i, w1, w2, w)
        c = c + d
        print(d)
        # print(i)
    print(c)


def part2(file_name: str) -> int:
    data = read_data(file_name)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667

    # answers
    # 1037554558406
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
