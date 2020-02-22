N,K = map(int,input().split())

A = []

for x in range (2,N+1) :
    A.append(x)
#print(A)

while K != 0 :
    P = min(A)
    for x in range (1,(int(N/P)+1)) :
        if P*x in A :
            A.remove(int(P*x))
            K-=1
            if K == 0 :
                print(P*x)
                break
