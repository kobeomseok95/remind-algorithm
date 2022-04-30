def solution(name):
    answer = 0
    not_a_idx = 0
    move = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        not_a_idx = i + 1
        while not_a_idx < len(name) and name[not_a_idx] == 'A':
            not_a_idx += 1

        move = min(
            move,
            (len(name) - not_a_idx) * 2 + i,
            i + i + len(name) - not_a_idx
        )

    return answer + move
