def solution(lottos, win_nums):
    rank_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    lottosSet = set(lottos)
    winNumsSet = set(win_nums)
    intersectCount = len(lottosSet.intersection(winNumsSet))
    zeroCount = lottos.count(0)
    return [rank_dict[intersectCount + zeroCount], rank_dict[intersectCount]]


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
