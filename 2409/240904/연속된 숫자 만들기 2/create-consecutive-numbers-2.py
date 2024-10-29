array = list(map(int, input().split()))
array.sort()

if array[0] + 1 == array[1] and array[1] + 1 == array[2]:
    print(0)
elif array[0] + 2 == array[1] or array[1] + 2 == array[2]:
    print(1)
else:
    print(2)