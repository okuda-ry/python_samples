X,Y = map(int,input().split())
for i in range(X+1):
    for j in range((X+1)-i):
        k = X - i - j
        if 10000*i + 5000*j + 1000*k == Y:
            print(i,j,k)
            exit()

print(-1,-1,-1)