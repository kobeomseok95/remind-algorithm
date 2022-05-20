def solution(n, words):
    previous_words = set()
    previous_words.add(words[0])
    for i in range(1, len(words)):
        if words[i] in previous_words or words[i - 1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
        previous_words.add(words[i])
    return [0, 0]
