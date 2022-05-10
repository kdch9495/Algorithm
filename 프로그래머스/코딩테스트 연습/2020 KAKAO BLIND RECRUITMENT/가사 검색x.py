# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3

# 효율성 테스트 실패1
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

# 효율성 테스트 실패1
def solution(words, queries):
    from collections import deque
    answer = []
    
    for query in queries:
        print(query)
        cnt = 0
        tmp_q = deque()
        len_q = deque()
        for i in range(len(query)):
            if query[i] != "?":
                tmp_q.append(i)
            elif query[i] == "?":
                len_q.append(i)

        for word in words:
            if tmp_q[0] == 0:
                if len(query) == len(word):
                    if query[:int(len_q[0])] == word[:int(len_q[0])]:
                        cnt += 1
            elif len_q[0] == 0:
                if len(query) == len(word):
                    if query[int(tmp_q[0]):] == word[int(tmp_q[0]):]:
                        cnt += 1

        answer.append(cnt)
    return answer 
