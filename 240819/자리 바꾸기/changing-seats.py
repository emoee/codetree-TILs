n, k = map(int, input().split())

person = [0] * (n+1)
counts = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    person[i] = i
    counts[i][i] = 1

order = []
for i in range(k):
    a, b = map(int, input().split())
    order.append((a,b))

for i in range((k*3)):
    a, b = order[i%k]
    person[a], person[b] = person[b], person[a]
    for j in range(1, n+1):
        counts[person[j]][j] = 1

for c in range(1, n+1):
    print(sum(counts[c]))