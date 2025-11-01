c = [list(map(int, input().split())) for _ in range(3)]

p = 1
for i in range(3):
    if c[i][0] == c[i][1] or c[i][1] == c[i][2] or c[i][2] == c[i][0]:
        p *= 2 / 3

for i in range(3):
    if c[0][i] == c[1][i] or c[1][i] == c[2][i] or c[2][i] == c[0][i]:
        p *= 2 / 3

if c[0][0] == c[1][1] or c[1][1] == c[2][2] or c[2][2] == c[0][0]:
    p *= 2 / 3

if c[0][2] == c[1][1] or c[1][1] == c[2][0] or c[2][0] == c[0][2]:
    p *= 2 / 3

print(p)
