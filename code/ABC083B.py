def main():
    N,A,B = map(int,input().split())
    res = 0
    for i in range(1,N+1):
        tmp = sum(map(int,str(i))) 
        if A <= tmp <= B:
            res += i

    # print(sum(i for i in range(1, N+1) if A <= sum(map(int, str(i))) <= B))
    print(res)
    return

if __name__ == "__main__":
    main()
