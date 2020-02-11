A = int(input())
B = int(input())
C = int(input())

D = A*B*C

E = [0 for x in range(10)]

D = str(D)

for x in range (len(D)) :
    for y in range (0,10) :
        if int(D[x]) == y :
            E[y] += 1

for x in range (len(E)) :
    print(E[x])
