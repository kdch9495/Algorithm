# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    answer = [0]
    cnt = 0
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][(moves[i]-1)] != 0:
                answer.append(board[j][(moves[i]-1)])
                
                if answer[-2] == board[j][(moves[i]-1)]:
                    del answer[-2:]
                    cnt += 2
                    
                board[j][(moves[i]-1)] = 0
                
                break

    return cnt


"""
# 스택 : pop을 활용한 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
"""

"""
board
[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]]

moves
[1,5,3,5,1,2,1,4] # board[y][x-1] 열은 고정됨
[0][0], [1][0] [2][0] [3][0] -> 4
[0][4], [1][4]

뽑은 것
[4,3,1,1,3,2,0,4] -> 
4,3,3,2,4
4,2,4

-> [1,1,3,3] 터진 것(answer)
"""
