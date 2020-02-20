N = int(input())

A = [0 for x in range (N)]
DP = [1 for x in range (N)]

for x in range (N) :
    A[x] = int(input())

tmp = 0
for i in range (1,N) :
    for j in range (0,i) :
        if A[i] > A[j] :
            if DP[i] < DP[j]+1 :
                DP[i] = DP[j]+1

print(N-max(DP))
