# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(n):
    answer = []
    result = []
    for j in range(len(n)-1): # len = 3
        for i in range(j+1, len(n)):
            answer.append(n[j]+n[i])
    
    answer.sort()
    print(answer)
    
    for i in answer:
        if result[-1:] != [i]:
            result.append(i)
            
    return result

"""
*** sorted, set 사용한 코드 ***

def solution(numbers):
    sum_set = set([])

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_set.add(numbers[i]+numbers[j])
    return sorted(list(sum_set))
"""
