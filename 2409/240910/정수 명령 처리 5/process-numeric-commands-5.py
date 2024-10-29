def push_back(arr, x):
    arr.append(int(x))
    return arr

def pop_back(arr):
    return arr.pop()

def sizeA(arr):
    return len(arr)

def getK(arr, x):
    return arr[int(x)-1]
    
n = int(input())
array = []

for i in range(n):
    says = list(map(str, input().split(" ")))
    say = says[0]

    if say == "push_back":
        push_back(array, says[1])
    elif say == "pop_back":
        pop_back(array)
    elif say == "size":
        print(sizeA(array))
    elif say == "get":
        print(getK(array, says[1]))