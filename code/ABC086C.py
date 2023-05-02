N = int(input())
t = [list(map(int,input().split())) for i in range(N)]

tmp = [0,0,0]
for i in range(N):
    tmp = list(map(lambda x,y:abs(x-y) ,t[i],tmp))
    if (tmp[0] >= sum(tmp[1:])) and (tmp[0] - sum(tmp[1:])) % 2 == 0:
        continue
    else:
        print("No")
        exit()
print("Yes")
