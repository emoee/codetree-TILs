n, k = map(int, input().split())
person = list(range(n + 1))
counts = [set() for _ in range(n+1)]

order = []
for _ in range(k):
    a, b = map(int, input().split())
    order.append((a,b))

for i in range(1, n + 1):
    counts[i].add(i)

for _ in range(3):
    for a, b in order:
        person[a], person[b] = person[b], person[a]

        counts[person[a]].add(a)
        counts[person[b]].add(b)


for c in range(1, n+1):
    print(len(counts[c]))