A = [0 for x in range (4)]
B = [0 for x in range (4)]

A[0],B[0] = map(int,input().split())
A[1],B[1] = map(int,input().split())
A[2],B[2] = map(int,input().split())

if A[0] != A[1] and A[1] == A[2] :
    A[3] = A[0]
elif A[1] != A[2] and A[2] == A[0] :
    A[3] = A[1]
elif A[2] != A[0] and A[0] == A[1] :
    A[3] = A[2]

if B[0] != B[1] and B[1] == B[2] :
    B[3] = B[0]
elif B[1] != B[2] and B[2] == B[0] :
    B[3] = B[1]
elif B[2] != B[0] and B[0] == B[1] :
    B[3] = B[2]

print(A[3],B[3])
