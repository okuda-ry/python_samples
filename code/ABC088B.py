def main():
    N = int(input())
    a = list(map(int,input().split()))
    Alice_points = 0
    Bob_points = 0

    for i in range(1,N+1):
        if i % 2 == 1:
            Alice_points += max(a)
            a.remove(max(a))
        else :
            Bob_points += max(a)
            a.remove(max(a))
    print(Alice_points - Bob_points)
    return

if __name__ == "__main__":
    main()

# N = int(input())
# a = sorted(map(int, input().split()))[::-1]
# print(sum(a[::2])-sum(a[1::2]))