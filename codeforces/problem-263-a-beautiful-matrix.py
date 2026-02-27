r, c = 1, 1
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        if a[j] == 1:
            r, c = i + 1, j + 1
print(abs(r - 3) + abs(c - 3))
