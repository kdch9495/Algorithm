# arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라
# 10진수를 n진수로 바꾸기 : 나머지를 문자열로 취급하고 역순으로 다 더하기

def solution(n): # n을 r진수로 바꾸기(역순)
    base = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, 3) # 몫과 나머지
        base += str(mod)

    base = base[::-1]

    for i in range(len(base)):
        answer += int(base[i]) * (3**i)

    return answer


# int(string, N) 를 사용하여 10진수를 N진수로 변환 가능
"""
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
"""
