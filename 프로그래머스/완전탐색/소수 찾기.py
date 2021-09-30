# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

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

