xy = [(2, 4), (2, 2), (9, 2), (5, 4)]
xy = [
    (10, 9),
    (10, 10),
    (10, 11),
    (10, 12),
    (10, 13),
    (10, 14),
    (10, 15),
    (10, 15),
    (11, 15),
    (12, 15),
    (13, 15),
    (14, 15),
    (15, 15),
    (15, 15),
    (15, 14),
    (15, 13),
    (15, 13),
    (16, 13),
    (17, 13),
    (17, 13),
    (17, 14),
    (17, 15),
    (17, 15),
    (18, 15),
    (19, 15),
    (19, 15),
    (19, 14),
    (19, 13),
    (19, 12),
    (19, 11),
    (19, 10),
    (19, 10),
    (18, 10),
    (17, 10),
    (17, 10),
    (17, 9),
    (17, 9),
    (16, 9),
    (15, 9),
    (15, 9),
    (15, 10),
    (15, 11),
    (15, 11),
    (14, 11),
    (13, 11),
    (12, 11),
    (12, 11),
    (12, 10),
    (12, 9),
    (12, 9),
    (11, 9),
    (10, 9),
]

# EXPLODE X AND Y
def explode_xy(xy):
    xl = []
    yl = []
    for i in range(len(xy)):
        xl.append(xy[i][0])
        yl.append(xy[i][1])
    return xl, yl


def shoelace_area(x_list, y_list):
    a1, a2 = 0, 0
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    for j in range(len(x_list) - 1):
        a1 += x_list[j] * y_list[j + 1]
        a2 += y_list[j] * x_list[j + 1]
    l = abs(a1 - a2) / 2
    return a1, a2, l, abs(a1 - a2)


xy_e = explode_xy(xy)

A = shoelace_area(xy_e[0], xy_e[1])
print(A)


from pyproj import Geod

geod = Geod("+a=6378137 +f=0.0033528106647475126")
lons = [i[0] for i in xy]
lats = [i[1] for i in xy]
# lons = [-102.20253523916332, -101.59096157206567, -100.65438018473898, -101.90199046561818]
# lats = [37.21550522238942, 37.70825886273666, 36.93243398218993, 36.394249155143996 ]

poly_area, poly_perimeter = geod.polygon_area_perimeter(lons, lats)

print("area: {} , perimeter: {}".format(poly_area, poly_perimeter))
