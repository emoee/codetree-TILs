n = int(input())
Address = [
    tuple(map(str, input().split()))
    for _ in range(n)
]

Address.sort()
address = Address[len(Address)-1]
name, addr, city = address
print("name " + name)
print("addr" , addr)
print("city", city)