def solution(information, queries):
    info_dict = {}
    for lang in ['cpp', 'java', 'python', '-']:
        for position in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    info_dict[lang + position + career + food] = []

    for info in information:
        info_split = info.split()
        for lang in [info_split[0], '-']:
            for position in [info_split[1], '-']:
                for career in [info_split[2], '-']:
                    for food in [info_split[3], '-']:
                        info_dict[lang + position + career + food].append(int(info_split[4]))

    for key in info_dict.keys():
        info_dict[key].sort()

    answer = []
    for query in queries:
        query = query.replace(" and ", "")
        query, score = query.split()
        score = int(score)

        query_scores = info_dict[query]
        tmp = len(query_scores)
        low, high = 0, len(query_scores) - 1
        while low <= high:
            mid = (low + high) // 2
            if score <= query_scores[mid]:
                tmp = mid
                high = mid - 1
            else:
                low = mid + 1
        answer.append(len(query_scores) - tmp)
    return answer
