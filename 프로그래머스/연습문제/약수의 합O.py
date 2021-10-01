# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    set_list = set() #중복 안되게끔 set() 사용
    
    for i in range(n, 0, -1):
        if n % i == 0:
            set_list.add(i)
            set_list.add(n/i)
            
    
    for i in set_list:
        answer += i

    return answer

"""
풀이 최적화

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
"""
