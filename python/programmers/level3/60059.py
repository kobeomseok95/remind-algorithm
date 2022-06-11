def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)
    lock = create_extend_lock(key_len, lock_len, lock)
    return unlock(key_len, lock_len, key, lock)


def create_extend_lock(key_len, lock_len, lock):
    extend_lock = [[0] * (2 * key_len + lock_len) for _ in range(2 * key_len + lock_len)]
    for i in range(lock_len):
        for j in range(lock_len):
            extend_lock[i + key_len][j + key_len] = lock[i][j]
    return extend_lock


def unlock(key_len, lock_len, key, lock):
    for k in range(4):
        key = rotate(key_len, key)
        for i in range(1, key_len + lock_len):
            for j in range(1, key_len + lock_len):
                put(i, j, key_len, key, lock)
                if is_open(key_len, lock_len, lock):
                    return True
                take_out(i, j, key_len, key, lock)
    return False


def is_open(key_len, lock_len, lock):
    for i in range(lock_len):
        for j in range(lock_len):
            if lock[key_len + i][key_len + j] != 1:
                return False
    return True


def put(i, j, key_len, key, lock):
    for y in range(key_len):
        for x in range(key_len):
            lock[y + i][x + j] += key[y][x]


def take_out(i, j, key_len, key, lock):
    for y in range(key_len):
        for x in range(key_len):
            lock[y + i][x + j] -= key[y][x]


def rotate(M, key):
    new = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new[j][M - i - 1] = key[i][j]
    return new
