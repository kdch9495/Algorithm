# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    
    for i in range(len(str(n))):
        answer.append(int(str(n)[i]))
    
    # for i in str(n):
    #   answer.append(int(i)) 이렇게 해도 됨
    
    answer.reverse()
    
    return answer
