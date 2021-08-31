A = input()
B = input()
X = []
Y = []

DP = [[0 for x in range (len(A)+1)] for x in range (len(B)+1)]

for i in range (1,len(B)+1) :
    for j in range (1,len(A)+1) :
        if A[j-1] == B[i-1] :
            DP[i][j] = DP[i-1][j-1] + 1
        else :
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])
print(max(max(DP)))
