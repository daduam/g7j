n, t = map(int, input().split())
a = list(map(int, input().split()))
ans, cur, l = 0, 0, 0
for r in range(n):
    cur += a[r]
    while cur > t and l < r:
        cur -= a[l]
        l += 1
    if cur <= t:
        ans = max(ans, r - l + 1)
print(ans)
