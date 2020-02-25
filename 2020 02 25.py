A = [0 for x in range (3)]
for x in range (3) :
    A[x] = list(map(int,input().split()))

one = 0
answer = [0 for x in range (3)]
for i in range (3) :
    for j in range (4) :
        if A[i][j] == 0 :
            one += 1
    if one == 1 :
        answer[i] = 'A'
    elif one == 2 :
        answer[i] = 'B'
    elif one == 3 :
        answer[i] = 'C'
    elif one == 4 :
        answer[i] = 'D'
    else :
        answer[i] = 'E'
    one = 0
for x in range (3) :
    print(answer[x])
