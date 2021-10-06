# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit()  == True: # s가 정수로 이루져있는지 확인하기 위한 isdigit()
        answer = True
    else:
        answer = False
        
    return answer

"""
다른사람 풀이

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

"""
