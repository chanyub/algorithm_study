X,Y = map(int,input().split())

A = X
B = Y
while A != 0 and B != 0 :
    if A > B :
        A = A%B
    elif A < B :
        B = B%A
    else :
        break
if A != 0 :
    print(A)
    gong = int(Y/A)
    answer = X * gong
    print(answer)
elif B != 0 :
    print(B)
    gong = int(X/B)
    answer = Y * gong
    print(answer)
