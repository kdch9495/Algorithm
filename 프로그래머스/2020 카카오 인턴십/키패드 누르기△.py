# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = '' #"LR"로 이루어진 str

    # 손의 위치
    l_loc = 10 #location
    r_loc = 12
    
    for i in numbers:
        print(l_loc, r_loc)
        if i in [1,4,7]:
            answer += 'L'
            l_loc = i
        elif i in [3,6,9]:
            answer += 'R'
            r_loc = i
        elif i in [2,5,8,0]:
            if i == 0:
                i = 11
            
            #l r distance
            l_dis = sum(divmod(abs(l_loc - i), 3))
            r_dis = sum(divmod(abs(r_loc - i), 3))
            
            if l_dis < r_dis:
                answer += 'L'
                l_loc = i
            elif l_dis > r_dis:
                answer += 'R'
                r_loc = i            
            elif l_dis == r_dis:
                answer += hand[0].upper()
                if answer[-1:] == 'L': l_loc = i
                else: r_loc = i
            
    return answer

"""
다른 사람의 코드

def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
    
"""
