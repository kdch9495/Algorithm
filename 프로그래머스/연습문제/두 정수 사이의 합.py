# https://programmers.co.kr/learn/courses/30/lessons/12912

# 내가 한 풀이
def solution(a, b):
    answer = 0
    if a < b:
        x = a
        y = b
    else:
        x = b
        y = a
        
    for i in range(x, y+1):
        answer += i
        
    return answer

# 다른 풀이
def solution(a, b):
    answer = 0
    
    if a==b: return a		  # 두 수가 같으면 둘 중 하나인 a 리턴
    elif a>b: a,b=b,a		  # a가 더 크면 두 수를 서로 교환한다
    
    for i in range(a,b+1):	  #작은수부터 큰수까지
        answer+=i         	  #더해준다
    
    return answer

# 다른 풀이
def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
