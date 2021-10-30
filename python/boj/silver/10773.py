import sys


def input_stack(n):
    if n == 0:
        stack.pop()
    else:
        stack.append(n)


k = int(sys.stdin.readline().strip())
stack = []
for i in range(k):
    input_stack(int(sys.stdin.readline().strip()))

answer = 0
for s in stack:
    answer += s
print(answer)
