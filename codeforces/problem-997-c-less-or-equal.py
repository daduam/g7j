n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
candidate = a[max(0, min(n - 1, k - 1))]
ans = -1
for j in [-1, 0, 1]:
    count = 0
    if candidate + j < 1 or candidate + j > 10**9:
        continue
    for i in a:
        if i <= candidate + j:
            count += 1
    if count == k:
        ans = candidate + j
print(ans)
