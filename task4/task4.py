result = 0

with open('test.txt') as f:
    mas = list(map(int, f.readlines()))

target = sum(mas) // len(mas)

for i in mas:
    result += abs(i - target)
print(result)