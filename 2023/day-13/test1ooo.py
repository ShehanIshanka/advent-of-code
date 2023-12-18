f = open("input.txt")

grid = []
currGrid = []
smugCnt = 0

for x in f:
    if x != "\n":
        currGrid.append(x.strip())
    else:
        grid.append(currGrid)
        currGrid = []
grid.append(currGrid)


def checkSmugLines(i, j, data):
    first = data[i]
    second = data[j]
    diffCnt = 0
    for k in range(len(first)):
        if first[k] != second[k]:
            diffCnt += 1
        if diffCnt > 1:
            return -1
    if diffCnt == 1:
        return 1
    return 0


def findMirror(data):
    for i in range(len(data) - 1):
        global smugCnt
        smugCnt = 0
        smugCnt = checkSmugLines(i, i + 1, data)
        if smugCnt == -1:
            continue
        res = checkSame(i, i + 1, data)
        if res < 1 and smugCnt == 0:
            continue
        elif res == 1 or smugCnt == 1:
            if i == 0 and smugCnt == 1:
                return i + 1
            val = loopThough(i, data)
            if val == -1 or smugCnt == 0:
                continue
            if smugCnt == 1:
                return val
            # elif : continue
            # elif: return -1
    return -1


def checkSame(k, n, lines):
    global smugCnt
    if k >= 0 and n < len(lines):
        wasSmug = checkSmugLines(k, n, lines)
        if wasSmug == -1:
            return -1
        if wasSmug:
            if smugCnt > 0:
                return -1
            else:
                smugCnt += 1
                return 1

        if lines[k] == lines[n]:
            return 1
        else:
            return -1
    return 0


def loopThough(i, data):
    idx = 0
    for j in range(i, 0, -1):
        idx += 1
        cellRes = checkSame(i - idx, i + idx + 1, data)
        if cellRes == -1:
            return -1
        elif cellRes == 0:
            return i + 1
    return i + 1


cnt = 0
id = 0
for x in grid:
    id += 1
    res = findMirror(x)
    if res == -1:
        data = list(map(list, zip(*x)))
        res = findMirror(data)
        if res == -1:
            print("No sol found for:", id)
        else:
            print("line ", id, "found ver sol at ", res)
        cnt += res
    else:
        print("line ", id, "found hor sol at ", res)

        cnt += res * 100

# My time and rank:
print("Part2:", cnt)  # 04:20:26    8589
