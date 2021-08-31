import math

N, a, b = map(int,input().split())

answer = 1

while (a != 1 and b !=2 ) or (a != 2 and b != 1) :
    if a%2 == 0 :
        if a-1 == b :
            print(answer)
            break
        else :
            answer += 1
    elif a%2 == 1 :
        if a+1 == b :
            print(answer)
            break
        else :
            answer += 1

    a = math.ceil(a/2)
    b = math.ceil(b/2)
