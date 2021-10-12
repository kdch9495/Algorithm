def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("x")
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
            break

"""
1. 효율성 테스트에서 실패
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in completion:
        participant.remove(i)
        continue
    return participant[0]
    
"""
