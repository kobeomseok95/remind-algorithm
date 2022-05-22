from itertools import product


def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        for prod in list(product(vowels, repeat=i)):
            dictionary.append(''.join(prod))
    dictionary.sort()
    return dictionary.index(word) + 1


if __name__ == "__main__":
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
