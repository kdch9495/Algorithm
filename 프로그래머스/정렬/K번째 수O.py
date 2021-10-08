# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        temp = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(temp[commands[i][2]-1])
        
    return answer

"""
1. list, map, lambda 활용한 코드

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



2. 깔끔하고 가독성 좋은 코드

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
"""
