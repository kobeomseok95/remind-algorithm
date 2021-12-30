import sys
read = sys.stdin.readline


N = int(read())
building = []
for _ in range(N):
    building.append(int(read()))

stack = []
results = [0] * N
for idx, val in enumerate(building):
    while stack and val >= building[stack[-1]]:
        pop_idx = stack.pop()
        results[pop_idx] = idx - pop_idx - 1
    stack.append(idx)

while stack:
    pop_idx = stack.pop()
    results[pop_idx] = N - pop_idx - 1

print(sum(results))
