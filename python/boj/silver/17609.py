import sys
read = sys.stdin.readline


def is_palindrome(word):
    return word == word[::-1]


def solve(word, left, right):
    if is_palindrome(word):
        return 0

    while left < right:
        if word[left] != word[right]:
            if is_palindrome(word[left + 1: right + 1]):
                return 1
            elif is_palindrome(word[left: right]):
                return 1
            else:
                return 2
        left += 1
        right -= 1


answer = []
t = int(read().strip())

for _ in range(t):
    word = read().strip()
    answer.append(solve(word, 0, len(word) - 1))

for a in answer:
    print(a)
