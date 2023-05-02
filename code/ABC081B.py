def main():
    n = int(input())
    A = list(map(int,input().split()))
    tmp = 0
    while all(a % 2 == 0 for a in A):
        A = [a / 2 for a in A]
        tmp += 1
    print(tmp)
    return

if __name__== "__main__":
    main()