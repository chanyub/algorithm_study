N = int(input())
A = []
stack = []
for x in range (N) :
    A += input().split()

#print(A)

for x in range (len(A)) :
    if A[x] == 'push' :
        stack.append(A[x+1])
        #print(A[x+1])
    elif A[x] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
    elif A[x] == 'size' :
        print(len(stack))
    elif A[x] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif A[x] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
            del stack[-1]
