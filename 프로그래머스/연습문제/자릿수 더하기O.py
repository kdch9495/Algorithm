# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    
    for i in range(10):
        answer += n % 10
        n = n // 10

    return answer

"""
센스있는 답변
def solution(n):
    return sum(map(int,str(n)))
"""
