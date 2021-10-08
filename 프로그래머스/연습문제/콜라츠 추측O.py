# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(n):
    answer = -1
    
    for i in range(500):
        if n == 1:
            answer = i
            break
        else:
            n = n/2 if n%2 == 0 else (n*3) + 1
        
    return answer

"""
처음 했는데 테스트 13에서 계속 막힘
def solution(n):
    answer = -1
    cnt = 0
    
    while cnt < 500:
        if n % 2 == 0: # 짝수라면
            n = n/2
        else: # 홀수라면
            n = (n*3) + 1
        cnt += 1
        
        if n == 1:
            answer = cnt
            break
            
    return answer
"""
