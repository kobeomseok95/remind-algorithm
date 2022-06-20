answer = 0
def solution(begin, target, words):
    dfs(0, begin, target, words)
    return answer


def dfs(count, word, target, words):
    global answer
    if word == target:
        answer = count
        return
    for idx, next_word in enumerate(words):
        if is_different_one_character(word, next_word):
            dfs(count + 1, next_word, target, words[:idx] + words[idx + 1:])


def is_different_one_character(source, target):
    if len(source) != len(target):
        return False
    diff_count = 0
    for i in range(len(source)):
        if source[i] != target[i]:
            diff_count += 1
        if diff_count >= 2:
            return False
    return True
