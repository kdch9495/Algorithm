# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    su = "수"
    bak = "박"
    result = ""
    
    for i in range(n):
        if i % 2 == 0:
            result += su
        else:
            result += bak
                
    answer = result
    return answer
