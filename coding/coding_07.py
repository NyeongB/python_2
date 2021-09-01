'''
문제 : 완료하지 못한 선수
날짜 : 21.08.31
'''
def solution(participant, completion):
    
    d = {}
    
    answer = ''
    
    for i in participant:
        d[i] = d.get(i,0)+1
    
    for i in completion:
        if d.get(i) > 0:
            d[i] -= 1
    
    for i in participant:
        if d[i] >= 1:
            answer = i
        
        
    return answer