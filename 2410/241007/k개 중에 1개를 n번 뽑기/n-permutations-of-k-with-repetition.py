k, n = map(int, input().split())
answer = []

def Choose(start):
    if len(answer) >= n:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, k+1):
        answer.append(i)
        Choose(start+1)
        answer.pop()

    return

Choose(1)