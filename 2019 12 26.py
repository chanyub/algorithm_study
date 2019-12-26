def solution(n):
    if (n == 0) :
        answer = 0
    elif (n == 1) :
        answer1 = 1
    elif (2 <= n <= 100000) :
        a =  0
        b = 1
        while n!=1 :
            c = a + b
            a = b
            b = c
            n = n-1
        return c%1234567
    else : return ("error")
n = int(input())
print(solution(n))
