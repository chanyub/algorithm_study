NK = input().split()
N = int(NK[0])
K = int(NK[1])
A = []
for x in range (N) :
    A.append(int(input()))

tmp = 0
for x in range (-1,-(N+1),-1) :
    if K / A[x] != 0 :
        tmp += K // A[x]
        K = K % A[x]
    else :
        continue
        if K == 0 :
            break
print(tmp)
