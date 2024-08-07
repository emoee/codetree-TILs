student = [
    (tuple(map(str, input().split())))
    for _ in range(5)
]
student.sort(key=lambda x : x[0])
print("name")
for _ in student:
    print(" ".join(map(str, _)))
print()
student.sort(key=lambda x : -int(x[1]))
print("height")
for _ in student:
    print(" ".join(map(str, _)))