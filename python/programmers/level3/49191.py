from collections import deque


def solution(n, results):
    winners = [[] for _ in range(n + 1)]
    losers = [[] for _ in range(n + 1)]
    for win, lose in results:
        winners[win].append(lose)
        losers[lose].append(win)

    answer = 0
    for i in range(1, n + 1):
        visit = [False] * (n + 1)
        visit[0] = True
        visit[i] = True
        for result_record in [winners, losers]:
            player_queue = deque()
            player_queue.append(i)
            while player_queue:
                player_no = player_queue.popleft()
                for target_player_no in result_record[player_no]:
                    if not visit[target_player_no]:
                        visit[target_player_no] = True
                        player_queue.append(target_player_no)
        answer += 1 if False not in visit else 0
    return answer
