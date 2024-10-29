x1, x2, x3, x4 = map(int, input().split())

answer = "intersecting"
if x2 < x3 or x4 < x1:
    answer = 'nonintersecting'

print(answer)