# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    list = []
    
    for i in range(s.count(' ')+1): # 공백 제외하고 list 안에 넣기
        list.append(s.split(' ')[i])
        
    for j in range(len(list)):
        for i in range(len(list[j])):
            if i % 2 != 0: # 홀수번째일때, 소문자로 치환, answer에 담음
                answer += list[j][i].replace(list[j][i], list[j][i].lower())
            else: # 짝수번째일때, 대문자로 치환, answer에 담음
                answer += list[j][i].replace(list[j][i], list[j][i].upper())
        answer += ' '
        
    return answer[:-1]
