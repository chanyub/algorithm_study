N = int(input())
A = [0 for x in range (N)]
for x in range (N) :
    A[x] = int(input())
DP = [0 for x in range (N)]
for x in range (N) :
    if x == 0 :
        DP[x] = A[x]
    elif x == 1 :
        DP[x] = A[x] + A[x-1]
    elif x == 2 :
        DP[x] = max(A[x-2] + A[x], A[x-1] + A[x])
    else :
        DP[x] = max(A[x] + A[x-1] + DP[x-3], A[x] + DP[x-2])
print(DP[-1])
