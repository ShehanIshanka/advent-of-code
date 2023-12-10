def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
        else:
            merged.append(current)

    return merged


def get_a_to_c_mapping(a_to_b, b_to_c):
    a_to_c = {}
    b_intervals = list(b_to_c.keys())
    merged_b_intervals = merge_intervals(b_intervals)

    for a_range in a_to_b:
        a_to_c[a_range] = (float("inf"), 0)

    for a_range, a_value in a_to_b.items():
        for b_range in merged_b_intervals:
            b_value = b_to_c[b_range]
            if a_range[0] <= b_range[1] and b_range[0] <= a_range[1]:
                a_to_c[a_range] = (
                    min(a_to_c[a_range][0], b_value[0]),
                    max(a_to_c[a_range][1], b_value[1]),
                )

    return a_to_c


# Given 'a-to-b' and 'b-to-c' mappings
a_to_b = {
    (0, 49): (0, 49),
    (50, 97): (52, 99),
    (98, 99): (50, 51),
    (100, float("inf")): (100, float("inf")),
}

b_to_c = {
    (0, 14): (39, 53),
    (15, 51): (0, 36),
    (52, 53): (37, 38),
    (54, float("inf")): (54, float("inf")),
}

# Get the 'a-to-c' mapping using the function
result_a_to_c = get_a_to_c_mapping(a_to_b, b_to_c)

# Display the computed 'a-to-c' mapping
print("Computed 'a-to-c' mapping:", result_a_to_c)


a_to_c = {
    (0, 14): (39, 53),
    (15, 49): (0, 34),
    (50, 51): (37, 38),
    (52, 97): (54, 99),
    (98, 99): (35, 36),
    (100, float("inf")): (100, float("inf")),
}
