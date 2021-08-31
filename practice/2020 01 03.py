n = int(input())
A = [0 for x in range (n)]
if n >= 1 :
    A[0] = 1
if n >= 2 :
    A[1] = 2
for x in range (2,n) :
    A[x] = A[x-1]+A[x-2]
print(A[n-1]%10007)
