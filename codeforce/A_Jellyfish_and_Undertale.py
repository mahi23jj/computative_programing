t = int(input())
for _ in range(t):
    a, b, n = map(int, input().split())
    arr = list(map(int, input().split()))
    total = b
    for x in arr:
        total += min(x, a - 1)

    print(total)
