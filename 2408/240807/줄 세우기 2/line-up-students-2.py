n = int(input())
A = [(x, y, i+1) for i in range(n) for x, y in [map(int, input().split())]]

A.sort(key=lambda x: (x[0], -x[1]))

for _ in A:
    print(" ".join(map(str, _)))