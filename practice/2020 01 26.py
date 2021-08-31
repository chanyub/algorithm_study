X = int(input())
tmp = 0
while X > 0 :
    if X >= 64 :
        X -= 64
        tmp += 1
    elif X >= 32 and X < 64:
        X -= 32
        tmp += 1
    elif X >= 16 and X < 32:
        X -= 16
        tmp += 1
    elif X >= 8 and X < 16:
        X -= 8
        tmp += 1
    elif X >= 4 and X < 8:
        X -= 4
        tmp += 1
    elif X >= 2 and X < 4:
        X -= 2
        tmp += 1
    elif X == 1 :
        X -= 1
        tmp += 1

print(tmp)
