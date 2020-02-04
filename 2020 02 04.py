from functools import reduce

def factorial(n) :
    return reduce(lambda x, y : x * y, range (1, n+1))


N = int(input())
A = [0 for x in range (N)]
B = [0 for x in range (N)]
for x in range (N) :
    A[x],B[x] = map(int,input().split())
print(A,B)
a = 0
b = 0
c = 0
for x in range (N) :
    a = B[x] - A[x]
    if a == 0 :
        print(1)
    else :    
        print(factorial(B[x]) // (factorial(A[x]) * factorial(B[x]-A[x])))
