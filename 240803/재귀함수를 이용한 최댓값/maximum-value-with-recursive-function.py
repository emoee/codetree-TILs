n = int(input())
s = list(map(int, input().split()))

def MaxValue(s, m, value):
    if m+1 == n:
        return value

    if s[m] > value:
        value = s[m]
    
    return MaxValue(s, m+1, value)

print(MaxValue(s, 0, s[0]))