n, m = map(int, input().split())

numbers = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    numbers[x].append(y)
    numbers[y].append(x)

def dfs(array):
    global count
    for value in numbers[array]:
        if not visited[value]:
            visited[value] = True
            dfs(value)

dfs(1)
print(visited.count(True)-1)