N = int(input())
DP = [1 for x in range (N)]
for x in range (2,N) :
    DP[x] = DP[x-1] + DP[x-2]
print(DP[N-1])
