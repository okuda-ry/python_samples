n = int(input())
d = list(map(int, input().split()))

for i in range(len(d)):
    tmp = 0
    for j in range(0, len(d) - i):
        tmp += d[i + j]
        print(f"{tmp}", end=" ")
    print()
