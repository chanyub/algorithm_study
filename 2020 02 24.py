T = int(input())
A = [0 for x in range(T)]
for x in range (T) :
    V,E = map(int,input().split())
    A[x] = 2-V+E

for x in range (T) :
    print(A[x])
