def solution(files):
    answer = []
    for idx, file in enumerate(files):
        head, number = separate_head_number(file)
        answer.append((file, head, number, idx))
    return [file_info[0] for file_info in sorted(answer, key=lambda x: (x[1], x[2], x[3]))]


def separate_head_number(file):
    head, number = '', ''
    idx = 0
    while idx < len(file):
        if not file[idx].isdigit():
            head += file[idx]
            idx += 1
        else:
            break
    while idx < len(file):
        if file[idx].isdigit():
            number += file[idx]
            idx += 1
        else:
            break
    return head.lower(), int(number)
