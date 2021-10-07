# https://programmers.co.kr/learn/courses/30/lessons/12901

#일단 월일이 365일 중 며칠인지 알기, 며칠인지 알았다면 그에 맞는 요일 선택
def solution(a, b):
    import datetime as dt
    date = 0
    list = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    if a == 1 and b == 1:
        date = 0
    else:
        date = (int(str(dt.datetime(2016,a,b)-dt.datetime(2016,1,1)  ).split(' ')[0])) % 7
    
    return list[date]


"""
다른 사람의 코드
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

print(getDayName(5,24))
"""
