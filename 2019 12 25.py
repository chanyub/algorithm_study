n = int(input())
i = 1;
s= 0;
tmp = 0;
for i in range (1,n+1) :
    s=0
    for j in range (i,n+1) :
        s += j
        if(s == n) :
            tmp += 1
        elif(s >n) :
            break
print(tmp)
