# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    list = []
    for j in range(len(arr1)):
        for i in range(len(arr1[0])):
            list.append((arr1[j][i]+arr2[j][i]))
        answer.append(list)
        list = []
            
    return answer

"""
다른 풀이1
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
    
다른 풀이2
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A
    
다른 풀이3
import numpy as np
def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()

다른 풀이4
def sumMatrix(A,B):
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return answer

다른 풀이5
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]
"""
