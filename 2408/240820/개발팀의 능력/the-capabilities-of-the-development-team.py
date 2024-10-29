numbers = list(map(int, input().split()))
n = 5
sumNumbers = sum(numbers)
result = sumNumbers
for i in range(n):
    for j in range(i+1, n):
        for k in range(n):
            if k != i and k != j:
                teamA = numbers[i] + numbers[j]
                teamB = numbers[k]
                teamC = sumNumbers - (teamA + teamB)

                maxTeam = max(teamA, teamB, teamC)
                minTeam = min(teamA, teamB, teamC)

                if teamA != teamB and teamB != teamC and teamA != teamC:
                    result = min(result, maxTeam-minTeam)
                    
if result == sumNumbers:
    result = -1

print(result)