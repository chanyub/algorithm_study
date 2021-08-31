N = int(input())

A = [0]
A += list(map(int,input().split()))
DP = [0 for x in range (N+1)]
for x in range (1,N+1) :
    if x == 1 :
        DP[x] = A[x]
    elif x == 2 :
        DP[x] = max(A[x-1]+A[x-1],A[x])
    else :
        DP[x] = A[x]
        for k in range (0,x+1) :
            if DP[x-k] + DP[k] > DP[x] :
                DP[x] = DP[x-k]+DP[k]
print(max(DP))
