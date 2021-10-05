# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []

    for i in arr:
        answer.append(i) #answer에 일단 그대로 추가
        
    arr.sort() # arr 오름차순 정렬
    answer.remove(arr[0]) # arr의 제일 작은 수 제거

    if len(arr) == 1:
        answer = [-1] #만약 리턴하려는 배열의 길이가 1 이하라면 [-1] 리턴

    return answer


"""
가장 직관적인 코드
def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist
"""
