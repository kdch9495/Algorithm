# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

# bfs1
def solution(numbers, target):
    # -1, +1한 값을 자료구조에 저장/ 새로운 값은 pop해서 삭제 / len(numbers)만큼 돌렸을 때 stop 후, 값 카운트
    from collections import deque
    tmp = [0]
    for nums in numbers:
        tmp2 = []
        for i in tmp:
            tmp2.append(i+nums)
            tmp2.append(i-nums)
        tmp = tmp2
        
    return tmp2.count(target)


# pythonic
def solution(numbers, target):
    from itertools import product
    tmp = [(x,-x) for x in numbers]
    rs = list(map(sum, product(*tmp)))
    return rs.count(target)
