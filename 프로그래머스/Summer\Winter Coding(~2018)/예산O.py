# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    
    for i in sorted(d):
        budget -= i
        answer += 1
        
        if budget < 0:
            answer -= 1
            break
            
    return answer

"""
다른사람의 코드
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


처음 한 코드
def solution(d, budget):
    answer = 0
    b_sum = 0
    
    for i in sorted(d):
        b_sum += i
        answer += 1
        
        if b_sum > budget:
            answer -= 1
            break
            
    return answer
"""
