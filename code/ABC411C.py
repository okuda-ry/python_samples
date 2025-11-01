n, q = map(int, input().split())
a = list(map(int, input().split()))

color = [1] * (n + 2)  # 両端をpadding
count = 0

# 二重ループにするとタイムアウト
# カウントの増減に着目する．
for i in a:
    color[i] = -1 if color[i] == 1 else 1

    if color[i] == -1:
        if color[i - 1] == 1 and color[i + 1] == 1:
            count += 1
        if color[i - 1] == -1 and color[i + 1] == -1:
            count -= 1
    if color[i] == 1:
        if color[i - 1] == -1 and color[i + 1] == -1:
            count += 1
        if color[i - 1] == 1 and color[i + 1] == 1:
            count -= 1
    print(count)
