# https://programmers.co.kr/learn/courses/30/lessons/12934

"""
math 함수 사용
math.ceil(i) : 올림
math.floor(i) : 내림
math.trunc(i) : 버림
"""

import math

def solution(n):
    answer = 0
    
    if (n ** 0.5) - math.trunc(n ** 0.5) == 0:
        answer = ((n ** 0.5) + 1) ** 2
    else:
        answer = -1

    return answer

"""
제일 간단한 풀이 
def solution(n):
    sqrt = n ** 0.5
    
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    else:
        return = -1
"""


