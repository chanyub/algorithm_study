A,B = map(str,input().split())

AA = []

max_A = 0
for x in range (len(A)) :
    if A[x] == '5' :
        AA.append(6)
    else :
        AA.append(A[x])
    max_A += int(AA[x])*(10**(len(A)-x-1))
#print(max_A)

BB = []

max_B = 0
for x in range (len(B)) :
    if B[x] == '5' :
        BB.append(6)
    else :
        BB.append(B[x])
    max_B += int(BB[x])*(10**(len(B)-x-1))
#print(max_B)

AA = []

min_A = 0
for x in range (len(A)) :
    if A[x] == '6' :
        AA.append(5)
    else :
        AA.append(A[x])
    min_A += int(AA[x])*(10**(len(A)-x-1))
#print(min_A)

BB = []

min_B = 0
for x in range (len(B)) :
    if B[x] == '6' :
        BB.append(5)
    else :
        BB.append(B[x])
    min_B += int(BB[x])*(10**(len(B)-x-1))
#print(min_B)

print(min_A+min_B,max_A+max_B)
