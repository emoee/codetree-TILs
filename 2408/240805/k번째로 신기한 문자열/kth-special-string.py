n, k, t = map(str, input().split())
result = []

for i in range(int(n)):
    T = input()
    if T[:len(t)] == t:
        result.append(T)

result.sort()
print(result[int(k)-1])