N = int(input())

s = "1"
for i in range(1, N + 1):
    for j in range(1, 10):
        if N % j == 0:
            if i % (N / j) == 0:
                s += str(j)
                break
        if j == 9:
            s += "-"

print(s)
