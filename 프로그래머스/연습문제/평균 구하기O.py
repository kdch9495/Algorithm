#https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):

    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    
    answer = sum/len(arr)
    
    return answer



# 다른 풀이
def solution(arr):
    answer = sum(arr) / len(arr)
    
    return answer
