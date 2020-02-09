n = int(input())

A = [0 for x in range (n+1)]

for x in range (1,n+1) :
    A[x] = int(input())

DP = [0 for x in range (n+1)]

for i in range (n+1) :
    if i == 1 :
        DP[i] = A[i]
    elif i == 2 :
        DP[i] = A[i] + A[i-1]
    elif i == 3 :
        DP[i] = max(A[i] + A[i-1], A[i-1] + A[i-2], A[i-2] + A[i])
    elif i >= 4 :
        DP[i] = max(A[i-1] + DP[i-3] + A[i], DP[i-2] + A[i],A[i-1] + DP[i-3], DP[i-2],DP[i-1])
print(max(DP))
