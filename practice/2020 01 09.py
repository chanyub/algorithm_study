import math

A,B,V = map(int,input().split())
x = V-A
y = math.ceil(x/(A-B))
print(int(y+1))
