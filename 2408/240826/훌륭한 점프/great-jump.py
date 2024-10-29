n, k = map(int, input().split())
numbers = list(map(int, input().split()))

MAXV = max(numbers)
result = MAXV

def possible(maxV):
    array = []
    values = []
    for index, value in enumerate(numbers):
        if value <= maxV:
            array.append(index)
            values.append(value)

    for p in range(1, len(array)):
        dist = array[p] - array[p-1]
        if dist > k:
            return False, values
    
    return True, values

for i in range(max(numbers[0], numbers[n - 1]), MAXV + 1):
    T, A = possible(i)
    if T and len(A) > 1:
        print(max(A))
        break