# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

# bfs1
def solution(numbers, target):
    answer = 0
    rs = [0]
    for num in numbers:
        tmp = []
        for val in rs:
            tmp.append(val+num)
            tmp.append(val-num)
        rs = tmp
    return rs.count(target)


# pythonic
def solution(numbers, target):
    from itertools import product
    tmp = [(x,-x) for x in numbers]
    rs = list(map(sum, product(*tmp)))
    return rs.count(target)
