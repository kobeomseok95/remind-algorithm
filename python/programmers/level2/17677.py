import math


def solution(str1, str2):
    snippet1 = makeSnippetList(str1)
    snippet2 = makeSnippetList(str2)
    return calculateAnswer(snippet1, snippet2)


def makeSnippetList(string):
    snippetList = list()
    string = string.lower()
    for i in range(len(string) - 1):
        snippet = string[i:i+2]
        if snippet.isalpha():
            snippetList.append(snippet)
    return snippetList


def calculateAnswer(snippets1, snippets2):
    set1 = set(snippets1)
    set2 = set(snippets2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return calculateSimilarity(snippets1, snippets2, intersection, union)


def calculateSimilarity(snippets1, snippets2, intersection, union):
    MULTIPLE = 65536

    if len(union) == 0:
        return MULTIPLE

    intersectionCount = 0
    unionCount = 0
    for i in intersection:
        intersectionCount += min(snippets1.count(i), snippets2.count(i))
    for u in union:
        unionCount += max(snippets1.count(u), snippets2.count(u))

    return math.floor((intersectionCount / unionCount) * MULTIPLE)


if __name__ == "__main__":
    print("===================================")
    print(solution("ab", "ab"))
    print("===================================")
    print(solution("+++", ""))
    print("===================================")
    print(solution("FRANCE", "french"))
    print("===================================")
    print(solution("handshake", "shake hands"))
    print("===================================")
    print(solution("aa1+aa2", "AAAA12"))
    print("===================================")
    print(solution("E=M*C^2", "e=m*c^2"))
