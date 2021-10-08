# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' #25
    
    for i in range(len(s)):
        for j in range(len(alpha)):
            if s[i] == " ":
                answer += " "
                break
            elif s[i].lower() == alpha[j]:
                answer += alpha[(j+n)] if s[i].islower() else (alpha[(j+n)]).upper()
                break
       
    return answer


"""
chr, ord 사용한 다른 코드
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.
"""
