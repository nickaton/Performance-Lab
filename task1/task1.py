import sys

n, m = int(sys.argv[1]), int(sys.argv[2])

mas = [i for i in range(1, n + 1)]
result = []
flag = 0
step = m

if m >= n:
    print('None')
elif m == 1:
    print(mas)
else:
    while True:
        result.append(mas[flag])
        flag += m
        flag %= n
        flag -= 1
        if flag == 0:
            break
    print(result)