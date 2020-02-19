A,B,C = map(int,input().split())

tmp = 0
answer = 0
while (1):
    a = B-A
    b = C-B
    if a == 1 and b == 1:
        break
    else :
        if b >= a :
            A = C-1
            tmp = A
            A = B
            B = tmp
        elif a > b :
            C = A+1
            tmp = C
            C = B
            B = tmp
        answer += 1
        #print(a,b)
        #print(A,B,C)
print(answer)
