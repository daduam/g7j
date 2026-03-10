n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
left = 0
runsum = 0
for right in range(n):
    runsum += a[right]
    while left <= right and runsum > s:
        runsum -= a[left]
        left += 1
    if runsum <= s:
        ans = max(ans, right - left + 1)
print(ans)
