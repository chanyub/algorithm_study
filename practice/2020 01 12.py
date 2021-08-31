N = int(input())
A = list(map(int,input().split()))
#print(A)

LD = [1 for x in range (N)]
RD = [1 for x in range (N)]

for i in range (1,N) :
    for j in range (0,i) :
        if A[i] > A[j] :
            if LD[j] + 1 > LD[i] :
                LD[i] = LD[j] + 1
#print(LD)

Ar = list(reversed(A))

#print(Ar)


for i in range (1,N) :
    for j in range (0,i) :
        if Ar[i] > Ar[j] :
            if RD[j] + 1 > RD[i] :
                RD[i] = RD[j] + 1

#print(RD)

answer = [0 for x in range (N)]
for x in range (N) :
    answer[x] = LD[x] + list(reversed(RD))[x] -1
print(max(answer))
