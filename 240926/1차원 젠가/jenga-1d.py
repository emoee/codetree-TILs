n = int(input())
jenga = [
    int(input()) for _ in range(n)
]

jenga.reverse()
arr = [0] * n
endArray = 0
endJenga = n

for _ in range(2):
    s, e = map(int, input().split())
    for i in range(s-1, e):
        jenga[endJenga-1-i] = 0

    for i in range(endJenga):
        if jenga[i] != 0:
            arr[endArray] = jenga[i]
            endArray += 1

    for i in range(endArray):
        jenga[i] = arr[i]

    endJenga = endArray
    endArray = 0

print(endJenga)
for i in range(endJenga-1, -1, -1):
    print(jenga[i])