N = int(input())
A = list(map(int,input().split()))
DP = [1 for x in range (N)]
tmp = 0
for i in range (1,N) :
    for j in range (0,i) :
        if A[i] < A[j] :
            if DP[j] + 1 > DP[i] :
                DP[i] = DP[j] + 1
            

print(max(DP))
