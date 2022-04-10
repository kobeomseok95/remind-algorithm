from collections import Counter


def solution(n, stages):
    result = dict()
    users = len(stages)
    count_users_per_stage = Counter(stages)
    for stage in range(1, n + 1):
        if users != 0:
            count = count_users_per_stage[stage]
            result[stage] = count / users
            users -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)
