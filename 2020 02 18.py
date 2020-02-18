N = int(input())
A = list(map(int,input().split()))
DP = [A[0] for x in range (N)]

for i in range (1,N) :
    DP[i] = A[i]
    tmp = 0
    for j in range (0,i) :
        if A[i] > A[j] :
            tmp = A[i]+DP[j]
            if tmp > DP[i] :
                DP[i] = tmp
            
print(max(DP))
