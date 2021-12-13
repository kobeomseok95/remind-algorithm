import sys
read = sys.stdin.readline


N = int(read())
arr = list(map(int, read().split()))
stack = [(1, arr[0])]
answer = [0]
for i in range(1, len(arr)):
    if stack[-1][1] < arr[i]:
        while stack and stack[-1][1] < arr[i]:
            stack.pop()
        if stack:
            answer.append(stack[-1][0])
        else:
            answer.append(0)
        stack.append((i + 1, arr[i]))
    else:
        answer.append(stack[-1][0])
        stack.append((i + 1, arr[i]))

for a in answer:
    print(a, end=' ')
