"""
rectangle

a, b = map(int, input().split())
print(f"{a*b} {2*(a+b)}")
"""

"""
watch

S = int(input())

print(f"{int(S/3600)}:{int((S/60)%60)}:{int(S%60)}")
"""

# 約数問題
# S = int(input())
# res = []
# for i in range(S):
#     if S % (i + 1) == 0:
#         res.append(i + 1)
# print(res)

N = int(input())
X = list(map(int, input().split()))
max_sum = float("-inf")
current_sum = 0
for i in X:
    current_sum = max(i, current_sum + i)
    max_sum = max(max_sum, current_sum)
print(max_sum)
