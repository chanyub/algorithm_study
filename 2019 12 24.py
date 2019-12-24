n = int(input())
if (n <1 or n >500) :
    print("error")
DP = [[0 for x in range (n)] for x in range (n)]
for x in range (n) :
        DP[x] += (input().split())
        del DP[x][:n]

for x in range (n) :
    for y in range (x+1) :
        DP[x][y] = int(DP[x][y])


for i in range(1,n) :
    for j in range(0,i+1) :
        if j == 0 :
            DP[i][j] += DP[i-1][j]
        elif i == j :
            DP[i][j] += DP[i-1][j-1]
        else :
            DP[i][j] += max(DP[i-1][j-1],DP[i-1][j])
print(max(DP[n-1]))
