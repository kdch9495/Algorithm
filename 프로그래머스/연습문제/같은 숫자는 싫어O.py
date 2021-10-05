# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(0, len(arr)):
        if i == 0: # arr[0]일때는 answer에 무조건 추가
            answer.append(arr[i])
        elif answer[len(answer)-1] != arr[i]: # 이후 answer의 가장 마지막 값과 arr[i]가 같지 않다면,
            answer.append(arr[i]) # answer에 arr[i]를 추가
    return answer


"""
최적화 코드
def solution(arr):
    answer = []

    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)

    return answer 
"""
