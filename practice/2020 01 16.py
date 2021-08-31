N = int(input())
A = [0]
A += list(map(int,input().split()))
tmp = [0 for x in range (N+1)]
result = -1001

for x in range (1,N+1) :
    tmp[x] = max(tmp[x-1] + A[x],A[x])
    result = max(result,tmp[x])
print(result)
