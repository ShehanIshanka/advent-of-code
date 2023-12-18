def shoelace_formula(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return abs(area) / 2.0


def shoelace_formula(polygonBoundary, absoluteValue=True):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [
        (polygonBoundary[i + 1][0] - polygonBoundary[i][0])
        * (polygonBoundary[i + 1][1] + polygonBoundary[i][1])
        for i in range(nbSegment)
    ]

    if absoluteValue:
        return abs(sum(l) / 2.0)
    else:
        return sum(l) / 2.0


# Example vertices representing a polygon (x, y)
polygon_vertices = [
    (0, 0),
    (4, 0),
    (4, 3),
    (3, 3),
    (3, 2),
    (0, 2),
    (0, 3),
    (0, 0),
]
polygon_vertices = [(0, 0), (0, 1)]

polygon_vertices1 = [
    (10, 9),
    (12, 9),
    (12, 11),
    (15, 11),
    (15, 9),
    (17, 9),
    (17, 10),
    (19, 10),
    (19, 15),
    (17, 15),
    (17, 13),
    (15, 13),
    (15, 15),
    (10, 15),
    (10, 10),
]

l = 5
d =5
grid1 = [["."] * l * 4 for i in range(d * 4)]
y = 0
for i, j in polygon_vertices1:
    grid1[i][j] = y
    y = y + 1

for x in grid1:
    print("".join(map(str, x)))
polygon_area = shoelace_formula(polygon_vertices1)
print(f"Area of the polygon: {polygon_area}")
