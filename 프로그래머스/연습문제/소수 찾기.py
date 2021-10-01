# https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

# 에라토스테네스의 체 사용
def solution(n):
    n = n+1 # 이렇게 안하면 첫번째가 씹힘
    prime_list = [True] * n # 소수는 True로 설정
    m = int(n ** 0.5) # n의 약수는 sqrt(n)이기 때문에 여기까지만 검사할 것임 (sqrt는 루트)
    cnt = 0 # True가 몇개인지 카운트하기 위한 변수
    
    for i in range(2, m+1): # 제곱한 것 안에서만 체크하면 됨
        if prime_list[i] == True: # i가 소수라면
            for j in range(i+i, n, i): # i 이후의 i의 배수들은 모두 False로 설정
                prime_list[j] = False
                
        
    for i in range(2, n):
        if prime_list[i] == True:
            cnt += 1
    
    answer = cnt
    return answer

"""
효율성 테스트에서 실패
def solution(n):
    cnt = 0
    answer = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i > 1 and i % j == 0:
                cnt += 1
                
        if cnt == 2:
            answer += 1
        
        cnt = 0
        
    return answer
"""
