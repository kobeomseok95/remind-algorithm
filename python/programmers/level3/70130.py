from collections import Counter


def solution(a):
    if len(a) <= 1:
        return 0

    count_arr = Counter(a)
    answer = -1
    for k, v in count_arr.items():
        if count_arr[k] * 2 < answer:
            continue

        idx = 0
        length = 0
        while idx < len(a) - 1:
            if (a[idx] == k and a[idx + 1] == k) or (a[idx] != k and a[idx + 1] != k):
                idx += 1
                continue

            idx += 2
            length += 2
        answer = max(answer, length)
    return answer
