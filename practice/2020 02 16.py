X,Y = map(str,input().split())

REVX = X[::-1]
REVY = Y[::-1]

answer = int(REVX)+int(REVY)
answer = str(answer)
answer = answer[::-1]
print(int(answer))
