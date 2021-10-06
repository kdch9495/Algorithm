def solution(s):
    s.lower()
    p_cnt = 0
    y_cnt = 0
    for i in s.lower():
        if i == "p":
            p_cnt += 1
        elif i == "y":
            y_cnt += 1
    
    return p_cnt == y_cnt

"""
다른 사람 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
"""

