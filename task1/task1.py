n, m = list(map(int, input().split()))
mas = [i for i in range(1, n + 1)]
result = [mas[0]]
flag_left = 0
flag_right = m - 1

if m > n:
    print('None')
else:
    while True:
        if mas[0] == mas[flag_right]:
            break
        else:
            result.append(mas[flag_right])
            flag_left = flag_right
            flag_right += m
            flag_right %= n
            flag_right -= 1
    print(result)