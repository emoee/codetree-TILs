class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

co, cr, se = map(str, input().split())
bomb = Bomb(co, cr, se)

print("code : " + bomb.code)
print("color : " + bomb.color)
print("second : " + bomb.second)