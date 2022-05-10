# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3

# 시간 초과
def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        for word in words:
            isWord = [True] * len(query)
            if len(word) == len(query):
                for i in range(len(word)):
                    if query[i] != "?":
                        if word[i] != query[i]:
                            isWord[i] = False
                            break
                if isWord.count(True) == len(word):
                    cnt += 1
        answer.append(cnt)
    return answer
