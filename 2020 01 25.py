while 1 :
    A,B = map(int,input().split())
    if A == 0 and B == 0 :
        break
    elif B%A == 0 and B > A:
        print("factor")
    elif A%B == 0 and A > B:
        print("multiple")
    else :
        print("neither")
