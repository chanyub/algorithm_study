N = int(input())

answer= 0
tmp = 7
for x in range (N+1) :
    if x == 0 :
        answer = 0
    elif x == 1 :
        answer = 5
    elif x == 2 :
        answer += tmp
    else :
        answer += (tmp+3)
        tmp += 3
print(answer%45678)
