import sys

path1 = sys.argv[1]
path2 = sys.argv[2]

with open(f'{path1}') as f:
    info = f.readlines()
    x_0, y_0 = list(map(float, info[0].split()))
    r = float(info[1])

with open(f'{path2}') as f:
    info = f.readlines()
    for line in info:
        x, y = list(map(float, line.split()))
        res = (x - x_0) ** 2 + (y - y_0) ** 2
        if res > r ** 2:
            print(2)
        elif res == r ** 2:
            print(0)
        else:
            print(1)