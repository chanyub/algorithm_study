'''
BOJ_9663
N-Queen
https://www.acmicpc.net/problem/9663
'''

def promising(col, i):
    k = 1
    flag = True
    while (k<i and flag) :
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)): # 같은 col or 같은 대각선이면 flag = False
            flag = False
        k += 1
    return flag

def n_queens (col, i):
    global answer
    n = len(col) - 1 # n은 0부터 시작
    if (promising(col, i)): # promising True면
        if (i == n): # 리프노드에 도착하면
            answer += 1
        else: # 계속 진행
            for j in range(1, n+1): # 1, 2, 3, 4
                col[i+1] = j # col[1] = 1, col[1] = 2, col[1] = 3, col[1] = 4
                n_queens(col, i+1)

answer = 0
N = int(input())
col = [0]*(N+1)
n_queens(col, 0)
print(answer)

'''
시간초과
'''