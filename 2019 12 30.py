def LL (A,m) :
	P = [0]*(m)
	P[0] = A[m-1]
	for i in range (1, m) :
		P[i] = P[i-1] + A[m-i-1]
	return max(P)

def RR (A,m) :
	Q = [0]*(len(A)-m)
	Q[0] = A[m]
	for j in range (1, len(A)-m) :
		Q[j] = Q[j-1] + A[m+j]
	return max(Q)

def max_sum(A, left, right):
	m = (left+right+1)//2
	M = 0
	if left >= right-1 :
		return (M)
	M = LL(A,m) + RR(A,m)
	return max(max_sum(A,left,m),max_sum(A,m,right),M)
	

A = [int(x) for x in input().split()]
if max(A) < 0 :
	print(max(A))
else :
	sol = max_sum(A, 0, len(A))
	print(sol)
