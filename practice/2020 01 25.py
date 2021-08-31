T = int(input())
N = [0 for x in range (T)]
for x in range (T) :
    N[x] = int(input())

for x in range (len(N)) :
    n = N[x]
    A = [0 for x in range (n)]
    for i in range (n) :
        if i == 0 :
            A[i] = 1
        elif i == 1 :
            A[i] = 2
        elif i == 2 :
            A[i] = 4
        else :
            A[i] = A[i-1] + A[i-2] + A[i-3]
    print(A[n-1])
