# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    temp = 0
    for j in range(len(answer)-1):
        for i in range(len(answer)-1): # 4만큼 : 0,1,2,3
            if answer[i] > answer[i+1]:
                temp = answer[i+1]
                answer[i+1] = answer[i]
                answer[i] = temp

    return answer if len(answer) != 0 else [-1
                                            
"""
제일 간단한 풀이
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""
