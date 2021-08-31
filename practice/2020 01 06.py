N = int(input())
A = list(map(int,input().split()))
print(A)

sosu = 0
for i in range (N) :
    if A[i] >=2 :
        x = A[i] - 1
        sosu += 1
        while x >= 2 :
            if A[i] % x == 0 :
                sosu -= 1
                break
            x -= 1
print(sosu)
