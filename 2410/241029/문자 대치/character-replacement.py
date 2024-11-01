string = input()

string = string.replace('XXXX', 'aaaa')
string = string.replace('XX', 'bb')

if 'X' in string:
    string = -1

print(string)