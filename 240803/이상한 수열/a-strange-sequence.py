n= int(input())

def function(f):
    if f  < 4:
        return f
    return function(f//3) + function(f-1)

print(function(n))