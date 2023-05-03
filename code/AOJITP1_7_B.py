n, x = map(int, input().split())
while n != 0 and x != 0:
    tmp_count = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    tmp_count += 1
    print(tmp_count)
    n, x = map(int, input().split())
