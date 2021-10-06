# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2-1]+s[len(s)//2]
    else:
        return s[len(s)//2]
    
"""
# 슬라이싱을 제대로 활용한 다른 답안
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
"""
