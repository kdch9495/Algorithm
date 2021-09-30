# https://programmers.co.kr/learn/courses/30/lessons/12940

"""
* 유클리드호제법 : 최대공약수, 최소공배수 구하는 방법
 - GCD(A,B) = 최대공약수
 - LCM(A,B) = 최소공배수
"""

def solution(n, m):
    n_default = n
    m_default = m
    
    if n < m:
        n, m = m, n
    
    Num = 0
    while True:
        if m == 0:
            break
        else:
            n, m = m, n%m
        Num = n
    
    answer = [Num, (n_default*m_default/Num)]
    return answer
