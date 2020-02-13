tmp = 0
for x in range (5) :
    A = int(input())
    if A < 40 :
        A = 40
    tmp += A

print(int(tmp/5))
