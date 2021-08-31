N = int(input())
#print(N)
n = 1
answer = 0

if N == 1 :
    print(1)
elif N >= 2 and N <= 7:
    print(2)
else :
    while 3*n*(n+1) < N-1 :
        n += 1
    answer = n + 1
    print(answer)
