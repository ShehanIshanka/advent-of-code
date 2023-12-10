def get_val(d, v):
    x = v
    for i, j in d.items():
        if i[0] <= v <= i[1]:
            x = j[0] + v - i[0]

    return x


def get_a_to_c_mapping(a_to_b, b_to_c):
    a_to_c = {}

    c = []
    for i in a_to_b.copy():
        if i[0] == i[1]:
            c.append(i[0])

    for i in b_to_c.copy():
        if i[0] == i[1]:
            c.append(i[0])

    a_keys_list = [item for sublist in a_to_b.keys() for item in sublist]
    b_keys_list = [item for sublist in b_to_c.keys() for item in sublist]
    full_list = list(a_keys_list + b_keys_list)
    full_list = sorted(full_list + list(set(c)))

    # if len(full_list) % 2 != 0:
    #     full_list[-2:] = [full_list[-2], full_list[-2] + 1, full_list[-1]]

    print(full_list)
    # print(full_list)
    for i in range(0, len(full_list), 2):
        a, b = full_list[i], full_list[i + 1]
        a_to_c[(a, b)] = (
            get_val(b_to_c, get_val(a_to_b, a)),
            get_val(b_to_c, get_val(a_to_b, b)),
        )

    return a_to_c


# Example usage:
a_to_b = {
    (0, 15): (0, 50),
    # (15, 15): (50, 50),
    (16, 97): (53, 99),
    (98, 99): (51, 52),
    (100, float("inf")): (100, float("inf")),
}

b_to_c = {
    (0, 14): (39, 53),
    (15, 51): (0, 36),
    # (51, 51): (36, 36),
    (52, 53): (37, 38),
    (54, float("inf")): (54, float("inf")),
}

a_to_c = {
    (0, 14): (39, 53),
    (15, 49): (0, 34),
    (50, 51): (37, 38),
    (52, 97): (54, 99),
    (98, 99): (35, 36),
    (100, float("inf")): (100, float("inf")),
}

# Get the 'a-to-c' mapping using the function
result_a_to_c = get_a_to_c_mapping(a_to_b, b_to_c)

# Display the computed a-to-c mapping
print(result_a_to_c)
print(a_to_c)
print(result_a_to_c == a_to_c)
