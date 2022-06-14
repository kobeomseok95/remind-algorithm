def solution(n, k, cmd):
    linked_list = create_linked_list(n)
    return cmd_process(linked_list, k, cmd)


def create_linked_list(n):
    linked_list = dict()
    for i in range(n):
        if i == 0:
            linked_list[i] = [None, 1]
        elif i == n - 1:
            linked_list[i] = [i - 1, None]
        else:
            linked_list[i] = [i - 1, i + 1]
    return linked_list


def cmd_process(linked_list, k, cmd):
    answer = ["O"] * len(linked_list)
    delete_idx = []
    for line in cmd:
        line = line.split(" ")
        if len(line) == 1:
            if line[0] == 'C':
                answer[k] = 'X'
                delete_idx.append(k)
                pre, nxt = linked_list[k]
                if nxt is None:
                    linked_list[pre][1] = None
                elif pre is None:
                    linked_list[nxt][0] = None
                else:
                    linked_list[pre][1] = nxt
                    linked_list[nxt][0] = pre
                k = linked_list[k][0] if linked_list[k][1] is None else linked_list[k][1]
            else:
                idx = delete_idx.pop()
                answer[idx] = 'O'
                pre, nxt = linked_list[idx]
                if pre is None:
                    linked_list[nxt][0] = idx
                elif nxt is None:
                    linked_list[pre][1] = idx
                else:
                    linked_list[nxt][0] = idx
                    linked_list[pre][1] = idx
        else:
            count = int(line[1])
            while count > 0:
                k = linked_list[k][0] if line[0] == 'U' else linked_list[k][1]
                count -= 1
    return ''.join(answer)
