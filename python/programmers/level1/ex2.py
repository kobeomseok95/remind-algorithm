def solution(n):
    n = str(n)
    wordArr = list(n)
    wordArr.sort(reverse=True)
    sortedStr = ''.join(wordArr)
    return int(sortedStr)


if __name__ == "__main__" :
    print(solution(118372))
