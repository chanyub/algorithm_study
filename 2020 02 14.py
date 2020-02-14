N,M = map(int,input().split())

A = [0 for x in range (N+1)]

#print(A)

A[0] = [0 for x in range (M+1)]

for x in range (1,N+1) :
    A[x] = [0] + list(map(int,input().split()))
#print(A)

for i in range (1,N+1) :
    for j in range (1,M+1) :
        A[i][j] = max(A[i-1][j] + A[i][j], A[i][j-1] + A[i][j])
print(max(A[N]))
