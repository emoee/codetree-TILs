n = int(input())
students = list(input())

def dist():
    d = n
    for a in range(n):
        for b in range(a+1, n):
            if students[a] == '1' and students[b] == '1':
                d = min(d, abs(a-b))
    return d
    
result = 0
for i in range(n):
    if students[i] == '0':
        students[i] = '1'
        result = max(result, dist())
        students[i] = '0'

print(result)