N = int(input())
A = list(map(int,input().split()))

DP = [0 for x in range (N)]

tmp = -999
for i in range (N) :
    for j in range (i,N) :
        if i == 0 and sum(A[i:j+1]) >= DP[i]:
            DP[i] = sum(A[i:j+1])
        elif i >= 1 :
            DP[i] = DP[i-1] - A[i-1]
            if DP[i] <= 0 :
                if tmp <= sum(A[i:j+1]) :
                    tmp = sum(A[i:j+1])
                if j == N-1 :
                    DP[i] = tmp
                
print(max(DP))
