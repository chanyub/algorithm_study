N = int(input())
P = input().split()
for x in range (N) :
    P[x] = int(P[x])

P.sort()

answer = 0
for i in range (N+1) :
    for j in range (i) :
        answer += P[j]
        #print(j)
print(answer)
