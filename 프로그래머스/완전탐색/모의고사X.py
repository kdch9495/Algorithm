# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    winner = []
    
    list_1 = [1,2,3,4,5] #5
    list_2 = [2,1,2,3,2,4,2,5] #8
    list_3 = [3,3,1,1,2,2,4,4,5,5] #10
    
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for i in range(len(answers)): # 정답이면 "o"로 치환
        if answers[i] == list_1[i%5]:
            cnt_1 += 1
        if answers[i] == list_2[i%8]:
            cnt_2 += 1
        if answers[i] == list_3[i%10]:
            cnt_3 += 1
    
    answer = [cnt_1, cnt_2, cnt_3]
    
    for list, score in enumerate(answer):
        if score == max(answer):
            winner.append(list+1)
    
    return winner

"""
1. iterable을 무한 반복시키는 cycle 함수 사용한 코드

from itertools import cycle
def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]


2. enumerate 사용을 잘한 예

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""
