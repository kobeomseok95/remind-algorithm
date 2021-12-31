from heapq import heappush, heappop
import sys
read = sys.stdin.readline


N = int(read())
left, right = [], []
answer = []
for _ in range(N):
    num = int(read())
    if len(left) == len(right):
        heappush(left, -num)
    else:
        heappush(right, num)

    if right and -left[0] > right[0]:
        min_val = -heappop(right)
        max_val = -heappop(left)
        heappush(left, min_val)
        heappush(right, max_val)

    answer.append(-left[0])

for a in answer:
    print(a)
