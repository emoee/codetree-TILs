n = int(input())

heights = [
    int(input()) for _ in range(n)
]

cost = 1000

maxIndex = heights.index(max(heights))
minIndex = heights.index(min(heights))

for i in range(1, 100):
    heights[maxIndex] -= i
    for j in range(1, 100):
        heights[minIndex] += j
        value = (i*i) + (j*j)

        if 0 < heights[maxIndex] - heights[minIndex] < 18:
            # print(i,j,value, heights)
            cost = min(cost, value)

        heights[minIndex] -= j

    heights[maxIndex] += i 
    

print(cost)