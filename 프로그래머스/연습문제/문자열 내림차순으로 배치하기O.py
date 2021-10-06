# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    list = []
    for i in s:
        list.append(ord(i))
    
    list.sort(reverse=True)
    
    for i in list:
        answer += chr(i)
        
    return answer

"""
제일 간단한 풀이 : 문자도 sorted를 이용하면 정렬이 됨
def solution(s):
    return ''.join(sorted(s, reverse=True))
"""
