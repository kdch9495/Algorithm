# https://programmers.co.kr/learn/courses/30/lessons/12969

n, m = map(int, raw_input().strip().split(' '))

# 간단한 방식    
stars = ("*" * n)
print((stars+"\n")*m)

# for문 사용한 비효율적인 방식
# for i in range(m):
#     for j in range(n):
#         print("*",end="")
#     print("")
