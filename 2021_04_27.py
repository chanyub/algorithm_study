import sys
import heapq

N = int(input())
heap = []

for n in range (N):
    x = int(sys.stdin.readline()) # 반복적으로 입력받아야할 때, input보다 빠르다
    if x == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap)[1])
    else :
        heapq.heappush(heap, (-x, x))
        # heapq.heapify(heap)