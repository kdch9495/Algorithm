# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    
    # 방문하지 않았다면 DFS 사용하여 방문처리. 방문하지 않은 컴퓨터 찾으면 네트워크 개수 +1
    def DFS(i):
        visited[i] = 1
        for j in range(len(computers[i])):
            if computers[i][j] and not visited[j]:
                DFS(j)
    
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
            
    return answer
