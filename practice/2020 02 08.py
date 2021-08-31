N,X = map(int,input().split())
A = list(map(int,input().split()))
B = []

for x in range (N) :
    if A[x] < X :
        B.append(A[x])


for x in range (len(B)) :
    print(B[x],end=' ')
