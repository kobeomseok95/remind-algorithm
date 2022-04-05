def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = lottos.count(0)
    correct_count = 0
    for lotto in lottos:
        if lotto in win_nums:
            correct_count += 1

    return [rank[zero_count + correct_count], rank[correct_count]]


if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
    print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
    print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
