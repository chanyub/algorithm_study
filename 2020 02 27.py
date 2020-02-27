import math

I,h,w = map(int,input().split())

a = I/math.sqrt(h**2 + w**2)

print(int(h*a),int(w*a))
