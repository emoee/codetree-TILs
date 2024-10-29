n = int(input())
text = input()
result = 1

for i in range(1, n):
    twice = False

    for j in range(n - i + 1):
        for k in range(j+1, n - i + 1):
            same = True

            for l in range(i):
                if text[j+l] != text[k+l]:
                    same = False
            
            if same:
                twice = True
    if twice:
        result = i + 1
    else:
        break

print(result)