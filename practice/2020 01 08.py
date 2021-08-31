A,B,C = map(int,input().split())
#print(A,B,C)


if C-B <= 0 :
    print(-1)
else :
    x = A/(C-B)
    print(int(x)+1)
