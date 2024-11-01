n = int(input())
beautiful = 0

def check(count):
    global beautiful
    if count >= n:
        if count == n:
            beautiful += 1
        return
    
    for i in range(1, 5):
        check(count+i)

check(0)
print(beautiful)