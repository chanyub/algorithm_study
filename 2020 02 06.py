N = int(input())

DP = [[0 for x in range (10)] for x in range (N)]

for x in range (10) :
    DP[0][x] = x + 1


for x in range (1,N) :
    for y in range (10) :
        if y == 0 :
            DP[x][y] = 1
        else :
            DP[x][y] = DP[x-1][y] + DP[x][y-1]

print(max(max(DP))%10007)
