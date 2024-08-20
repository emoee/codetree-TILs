numbers = list(map(int, input().split()))
n = 5
sumNumbers = sum(numbers)
result = sumNumbers
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                teamA = numbers[i] + numbers[j]
                teamB = numbers[k] + numbers[l]
                teamC = sumNumbers - (teamA + teamB)

                maxTeam = max(teamA, teamB, teamC)
                minTeam = min(teamA, teamB, teamC)
                # print(teamA, teamB, teamC)
                if teamA != teamB and teamB != teamC and teamA != teamC:
                    result = min(result, maxTeam-minTeam)
                    
if result == sumNumbers:
    result = -1

print(result)