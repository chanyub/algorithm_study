#def function(X) :
#    X = int(input())

#    DP = [0 for x in range (X)]
#    DP[0] = 1
#    DP[1] = 1
#    DP[2] = 1
#    for x in range (3,X) :
#        DP[x] = DP[x-2] + DP[x-3]
#    return (DP[X-1])



T = int(input())

P = [0 for x in range (T)]

for x in range (T) :
    P[x] = int(input())

z = 0
while z < len(P) :
    if P[z] > 100 or P[z] <1 :
        print("error")
    else :
        DP = [0 for x in range (P[z])]
        DP[0] = 1
        if P[z] > 1 :
            DP[1] = 1
        if P[z] > 2 :
            DP[2] = 1
        for x in range (3,P[z]) :
            DP[x] = DP[x-2] + DP[x-3]
        print(DP[P[z]-1])
        z+=1
