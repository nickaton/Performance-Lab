import sys
import importlib

var = sys.argv[1]

result = 0

with open(var) as f:
    mas = list(map(int, f.readlines()))

target = sum(mas) // len(mas)

for i in mas:
    result += abs(i - target)
print(result)