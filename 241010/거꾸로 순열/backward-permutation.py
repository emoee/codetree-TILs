n = int(input())
result = []
answer = []
visited = [False] * (n+1)
def Choose(num):
    if num == n+1:
        result.append(" ".join(map(str, answer)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        
        answer.append(i)
        visited[i] = True
        Choose(num + 1)
        answer.pop()
        visited[i] = False

Choose(1)
result.sort(reverse=True)

for i in result:
    print(i)