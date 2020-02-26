N = int(input())

A = [0 for x in range (N+1)]
A[0] = 1
A[1] = 3
for x in range (2,N+1) :
        A[x] = A[x-2] + 2*A[x-1]
        if x >= 3 :
            A[x-3] = 0

print(max(A)%9901)
