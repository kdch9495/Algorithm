# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

""" 
공부한 내용
1. 에라토스테네스의 체 : 소수를 판별하는 알고리즘
2. brute force attack(무차별 대입 공격) : 암호학에서 사용
3. 파이썬 기본 라이브러리인 itertools(combinations, permutations, product)
 - ex) list = [0,1,2] 2개로 구성한다면,
 - combinations : 하나의 리스트에서 순차적으로 조합 ex) 01, 02, 12
 - permutations : 하나의 리스트에서 모두 조합 ex) 01, 02, 10, 12, 20, 21
 - product : 두개 이상의 리스트에서 모든 조합을 계산
4. map(function, iterable) 함수
 - 첫번째 매개변수 : 함수
 - 두번째 매개변수 : 반복가능한 자료형(리스트, 튜플)
 - map(적용시킬 함수, 적용할 값들)
5. set() 함수
 - list선언과 달리 중복을 제거할 수 있고 sum, min, max와 같이 바로 사용가능함
 - add/update, remove/discard로 추가 및 제거할 수 있음
"""

import itertools

# 소수체크
def prime_check(a):
    if(a<=1):
        return False
    for n in range(2,a):
        if a % n == 0:
            return False
    return True

def solution(numbers):
    
    # 집합에 permuation 통해 탐색하며 값 추가
    val_set = set()
    for i in range(len(numbers),0,-1):
        for val in list(map("".join, itertools.permutations(numbers,i))):
            if prime_check(int(val)) is True:
                val_set.add(int(val));
    
    return len(val_set)

