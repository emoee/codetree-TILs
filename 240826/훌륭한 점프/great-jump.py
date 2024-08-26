n, k = map(int, input().split())
numbers = list(map(int, input().split()))

result = numbers[0]
start = 0
end = n

def check(numbers, s, n, k):
    index = s+1
    if s+k < n:
        c = numbers[s+1]
        for i in range(s+1, s+k+1):
            if numbers[i] < c:
                index = i
    else:
        index = n-1

    return index


while 1:
    start = check(numbers, start, n, k)
    result = max(result, numbers[start])

    if start == n-1:
        break

print(result)