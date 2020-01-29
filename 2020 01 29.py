N = int(input())
A = [0 for x in range (N)]
B = [0 for x in range (N)]
C = [0 for x in range (N)]
for x in range (N) :
    A[x],B[x] = map(str,input().split())
    A[x] = A[x][::-1]
    B[x] = B[x][::-1]
    A[x] = int(A[x])
    B[x] = int(B[x])
    C[x] = A[x]+B[x]
    C[x] = str(C[x])
    C[x] = C[x][::-1]
    C[x] = int(C[x])

for x in range (N) :
    print(C[x])
