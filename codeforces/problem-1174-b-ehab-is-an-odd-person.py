n = int(input())
a = list(map(int, input().split()))
evenodd = [False, False]
for x in a:
    evenodd[x % 2] = True
if all(evenodd):
    a.sort()
print(' '.join(map(str, a)))
