"""
탐욕 알고리즘(Greedy Algorithm)은 최적해를 구하는데 사용되는 방법으로, 여러 경우 중 하나를 결정해야할 때 마다 그 순간 최적이라고 생각되는 것을 선택해 나가는 방식이다. 그 선택을 계속 수집하여 해답을 만들었다고 해서 최적이라는 보장은 없다. 
cf) Dynamic Algorithm : 모든 경우의 수를 계산하는 단점이 있어 탐욕법이 등장하였다.
쉬운건데 틀림
"""

def solution(n, lost, reserve):
    lost_only = set(lost) - set(reserve)
    re_only = set(reserve) - set(lost)
    
    for i in re_only:
        if i-1 in lost_only:
            lost_only.remove(i-1)
        elif i+1 in lost_only:
            lost_only.remove(i+1)
    
    return n-len(lost_only)


"""
# 다른 사람 풀이

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)



#정확성테스트에서 실패

def solution(n, lost, reserve):
    answer = n - len(lost)
    
    for i in lost:
        if len(reserve) == 0:
            break
        else:
            for j in reserve:
                if i-1 == j or i+1 == j:
                    answer += 1
                    reserve.remove(j)
                    break
    
    return answer

"""
