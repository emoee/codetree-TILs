k, n = map(int, input().split())

answer = []
def Choose(number):
    if number == n:
        print(" ".join(map(str, answer)))
        return

    for i in range(1, k+1):
        if len(answer) >= 2 and (answer[-1] == i and answer[-2] == i):
            continue

        answer.append(i)
        Choose(number + 1)
        answer.pop()

Choose(0)