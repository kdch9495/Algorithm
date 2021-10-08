# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    str_x = str(x) # x를 문자열로 변환
    sum_x = 0 # 문자열로 변환된 것을 더함
    
    for i in range(len(str_x)):
        sum_x += int(str_x[i])
        
    answer = True if x % sum_x == 0 else False
    
    return answer

"""
다른 사람의 한줄 코딩
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0
"""
