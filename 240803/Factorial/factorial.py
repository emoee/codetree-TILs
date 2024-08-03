n = int(input())

def factorial(f):
    if f == 1:
        return f
    return f * factorial(f-1)

print(factorial(n))