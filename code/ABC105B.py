n = int(input())
result = 0
for i in range(1, n + 1):
    tmp = 0
    if i % 2 == 0 or i < 105:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            tmp += 1
    if tmp == 8:
        result += 1
print(result)
