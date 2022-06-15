import sys
from collections import deque
read = sys.stdin.readline


def solution(K, friends_name_lengths):
    lengths = [0 for _ in range(21)]
    count = 0
    for i in range(2, 21):
        q = deque()
        for name_length in friends_name_lengths:
            q.append(name_length)
            if len(q) > K + 1:
                length = q.popleft()
                if length == i:
                    lengths[i] -= 1

            if name_length == i:
                if lengths[i] > 0:
                    count += lengths[i]
                lengths[i] += 1

    return count


if __name__ == "__main__":
    N, K = map(int, read().split())
    friends_name_lengths = [len(read().strip()) for _ in range(N)]
    print(solution(K, friends_name_lengths))
