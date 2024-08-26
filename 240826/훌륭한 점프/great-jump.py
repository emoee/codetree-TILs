n, k = map(int, input().split())
numbers = list(map(int, input().split()))

MAXV = max(numbers)
result = MAXV

def possible(maxV):
    current = 0
    while current < n - 1:
        next_pos = -1
        for j in range(1, k + 1):
            if current + j < n and numbers[current + j] <= maxV:
                next_pos = current + j
        if next_pos == -1:
            return False
        current = next_pos
    return True

for i in range(max(numbers[0], numbers[n - 1]), MAXV + 1):
    if possible(i):
        print(i)
        break