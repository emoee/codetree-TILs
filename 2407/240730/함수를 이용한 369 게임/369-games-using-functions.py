start, end = map(int, input().split())

def checked(number):
    stringN = str(number)
    if "3" in stringN or "6" in stringN or "9" in stringN:
        return True

count = 0
for i in range(start, end+1):
    if i % 3 == 0 or checked(i):
        count += 1

print(count)