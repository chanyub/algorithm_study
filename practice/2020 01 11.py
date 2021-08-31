N = int(input())
legs = [0 for x in range (N)]
chickens = [0 for x in range (N)]
for x in range (N) :
    legs[x], chickens[x] = map(int,input().split())
#print(legs,chickens)
answer_noleg = []
answer_leg = []
for x in range (N) :
    answer_noleg.append(chickens[x] * 2 - legs[x])
    answer_leg.append(chickens[x] - answer_noleg[x])
#print(answer_noleg,answer_leg)

for x in range (N) :
    print(answer_noleg[x],answer_leg[x])
