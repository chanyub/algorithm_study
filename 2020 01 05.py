A = []
while 1 :
    N = input().split()
    N[0] = int(N[0])
    N[1] = int(N[1])
    N[2] = int(N[2])

    if N[0] == 0 and N[1] == 0 and N[2] == 0 :
        break
    elif N[0] ** 2 + N[1] ** 2 == N[2] ** 2 or N[1] ** 2 + N[2] ** 2 == N[0] ** 2or N[2] ** 2 + N[0] ** 2 == N[1] ** 2:
        tmp = 1
    else :
        tmp = 0

    A.append(tmp)
#print(A)

for x in range (len(A)) :
    if A[x] == 1 :
        print("right")
    else :
        print("wrong")
