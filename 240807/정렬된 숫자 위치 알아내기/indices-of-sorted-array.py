n = int(input())
A = list(map(int, input().split()))
index = []
for i in range(len(A)):
    index.append((i, A[i]))

index.sort(key=lambda x: x[1])

# for i in range(n):
#     for j in range(n):
#         if A[i] == index[j][1]:
#             print(j+1, end=" ")
#             index.pop(j)
#             index.insert(j, (0,0))
#             break

distance = [0] * n
for d, (i, a) in enumerate(index):
    distance[i] = d+1

print(" ".join(map(str, distance)))