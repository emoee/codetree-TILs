s, c, n = map(str, input().split())

class Code:
    def __init__(self, secret_code, meeting_point, code_time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.code_time = code_time
    

code = Code(s, c, n)
print("secret code : " + code.secret_code)
print("meeting point : " + code.meeting_point)
print("time : " + code.code_time)