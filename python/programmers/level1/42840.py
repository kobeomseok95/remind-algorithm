def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if pattern1[idx % len(pattern1)] == answer:
            scores[0] += 1
        if pattern2[idx % len(pattern2)] == answer:
            scores[1] += 1
        if pattern3[idx % len(pattern3)] == answer:
            scores[2] += 1

    max_score = max(scores)
    for idx, score in enumerate(scores, start=1):
        if score == max_score:
            result.append(idx)
    return result
