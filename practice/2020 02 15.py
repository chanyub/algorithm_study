import math

M = int(input())
N = int(input())

answer = []

for x in range (M,N+1) :
    if math.sqrt(x) - int(math.sqrt(x)) == 0 :
        answer.append(x)
#print(answer)

if len(answer) == 0 :
    print(-1)
else :
    print(sum(answer))
    print(answer[0])
