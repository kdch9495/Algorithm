# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(s, n):
    answer = []
    
    for i in range(len(s)):
        s[i] = s[i][n]+s[i]
        
    s = sorted(s)
    
    for i in range(len(s)):
        answer.append(s[i][1:])
        
    return answer

"""
1차 시도. 정확성 테스트에서 실패
def solution(s, n):
    answer = []
    s_temp = []
    
    for i in s:
        s_temp.append(i[n:])
    
    for i in sorted(s_temp):
        for j in s:
            if i in j:
                answer.append(j)
                break
    return answer
    

2차 시도. 정확성 테스트에서 실패
def solution(s, n):
    answer = []
    
    return sorted(s, key=lambda x: x[n])
"""

