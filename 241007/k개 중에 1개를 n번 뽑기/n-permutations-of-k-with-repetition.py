k, n = map(int, input().split())
answer = []

def Choose(start):
    if start == k+1:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, n+1):
        answer.append(i)
        Choose(start+1)
        answer.pop()
    return

Choose(1)