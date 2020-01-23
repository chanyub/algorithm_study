K = int(input())
A = []

for x in range (K) :
    I = int(input())
    if I == 0 :
        del A[-1]
    else :
        A.append(I)
        
print(sum(A))
