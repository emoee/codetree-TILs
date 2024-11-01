n, m = map(int, input().split())

visited = [False for _ in range(11)]
answer = []
def Choose(num, cnt):
    # print(answer, visited)
    if cnt == m:
        print(" ".join(map(str, answer)))
        return
       
    for i in range(1, n+1):
        if visited[i] == False and num < i:
            answer.append(i)
            visited[i] = True
            Choose(i, cnt+1)
            answer.pop()
            visited[i] = False

Choose(0, 0)