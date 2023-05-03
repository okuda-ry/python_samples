s = input()
acgt = ["A", "C", "G", "T"]
tmp = 0
ans = 0
for i in range(len(s)):
    if s[i] in acgt:
        tmp += 1
        if ans < tmp:
            ans = tmp
    else:
        tmp = 0
print(ans)
