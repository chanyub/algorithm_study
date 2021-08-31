N = int(input())

DP = [0 for x in range (N)]
for x in range (N) :
    DP[x] = input().split()

for i in range (N) :
    for j in range (3) :
        DP[i][j] = int(DP[i][j])

for i in range (N-1) :
    for j in range (3) :
        DP[i+1][j] = min(DP[i+1][j]+DP[i][j-1],DP[i+1][j]+DP[i][j-2])

print(min(DP[N-1]))
