def solution(gems):
    N = len(gems)
    answer = [0, N - 1]
    gems_set = set(gems)
    gems_dict = {gems[0]: 1}
    start, end = 0, 0
    while 0 <= start < N and 0 <= end < N and start <= end:
        if len(gems_dict) == len(gems_set):
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            if gems_dict[gems[start]] == 1:
                del gems_dict[gems[start]]
            else:
                gems_dict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end >= N:
                break
            if gems[end] not in gems_dict:
                gems_dict[gems[end]] = 0
            gems_dict[gems[end]] += 1
    return [answer[0] + 1, answer[1] + 1]
