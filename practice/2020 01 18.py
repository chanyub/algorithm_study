x,y,w,h = map(int,input().split())

if x == 0 or y == 0 :
    print(0)
else :
    print(min(abs(w-x),abs(h-y),x,y))
