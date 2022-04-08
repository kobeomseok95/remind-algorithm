def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    has_only = lost.intersection(reserve)
    lost = lost.difference(has_only)
    reserve = reserve.difference(has_only)

    for r in reserve:
        front = r - 1
        back = r + 1
        if front in lost:
            lost.remove(front)
        elif back in lost:
            lost.remove(back)
    return n - len(lost)






























if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
    print(solution(10, [3, 4, 5], [1,2,3,4,5,6,7,8,9,10]))
