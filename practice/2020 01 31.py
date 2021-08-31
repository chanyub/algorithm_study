n = int(input())
DP = [0 for x in range (n)]
for x in range (n) :
    if x == 0 :
        DP[x] = 1
    elif x == 1 :
        DP[x] = 3
    else :
        DP[x] = DP[x-1] + 2*DP[x-2]
print(DP[n-1]%10007)
