def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if budget - i < 0:
            break
        budget -= i
        count += 1

    return count
