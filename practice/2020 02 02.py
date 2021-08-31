N = int(input())

DP = [999 for x in range (N+1)]


for x in range (N+1) :
    if x == 0 :
        DP[x] = 0
    if x == 1 :
        DP[x] = 0
    if x >= 3 and x % 3 == 0 :
        DP[x] = DP[int(x/3)] + 1
    if x >= 2 and x % 2 == 0 :
        if DP[int(x/2)] + 1 < DP[x] :
            DP[x] = DP[int(x/2)] + 1
    if x-1 >= 1 :
        if DP[x-1] + 1 < DP[x] :
            DP[x] = DP[x-1] + 1
print(DP[N])
