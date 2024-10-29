def plus(a, b):
    return "%d + %d = %d" % (a, b, a+b)

def minus(a, b):
    return "%d - %d = %d" % (a, b, a-b)

def div(a, b):
    return "%d / %d = %d" % (a, b, a/b)

def power(a, b):
    return "%d * %d = %d" % (a, b, a*b)

a, o, c = map(str, input().split())
a = int(a)
c = int(c)

if o == "+":
    print(plus(a, c))
elif o == "-":
    print(minus(a, c))
elif o == "/":
    print(div(a, c))
elif o == "*":
    print(power(a, c))
else:
    print(False)