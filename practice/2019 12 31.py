n = int(input())
DP = [0 for x in range (n+2)]
DP[0] = 0
DP[1] = 1

for x in range (2,n+2) :
    DP[x] = DP[x-2]+DP[x-1]
    if DP[x] > 15746 :
        DP[x] = DP[x] % 15746

print(DP[n+1])
