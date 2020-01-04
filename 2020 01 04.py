N = input()
M = int(N)

cycle = 0
C = 0
if M == 0 :
    print(1)
while int(N) != C :
    C = (M%10 * 10) + ((M//10 + M%10)%10)
    if int(N) == C :
        cycle += 1
        print(cycle)
    else :
        M = C
        cycle += 1
