t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    good = True
    for i in range(1, n):
        good = good and (a[i] - a[i-1] <= 1)
    print('YES' if good else 'NO')
