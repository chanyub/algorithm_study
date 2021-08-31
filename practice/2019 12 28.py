A = input().split('-')
#print(A)

B = [0 for x in range (len(A))]

for x in range (len(A)) :
    B[x] = A[x].split('+')
#print(B)

for x in range (len(A)) :
    if len(B[x]) > 1 :
        for y in range (len(B[x])) :
            B[x][y] = int(B[x][y])
    else :
        B[x][0] = int(B[x][0])
    
#print(B)

for x in range (len(A)) :
    if len(B[x]) > 1 :
        B[x][0] = sum(B[x])
#print(B)

X = [0 for x in range(len(A))]
for x in range (len(B)) :
    X[x] -= B[x][0]
#print(X)

X[0] = X[0]*(-1)
print(sum(X))
