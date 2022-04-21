import sys
read = sys.stdin.readline


def solution(trains_count, commands):
    trains = [0] * (trains_count + 1)
    for command in commands:
        order_number, train_number = command[0], command[1]
        if order_number == 1:
            trains[train_number] |= (1 << (command[2] - 1))
        elif order_number == 2:
            trains[train_number] &= ~(1 << (command[2] - 1))
        elif order_number == 3:
            trains[train_number] = trains[train_number] << 1
            trains[train_number] &= ((1 << 20) - 1)
        elif order_number == 4:
            trains[train_number] = trains[train_number] >> 1
    return len(set(trains[1:]))


if __name__ == "__main__":
    n, m = map(int, read().split())
    commands = [list(map(int, read().split())) for _ in range(m)]
    print(solution(n, commands))
