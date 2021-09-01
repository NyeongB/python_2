'''
문제 : 체육복
날짜 : 21.08.31
'''

def solution(n, lost, reserve):
    answer = n
    
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)
    answer -= len(lostSet)
    for i in lostSet:
        if i - 1 in reserveSet:
            reserveSet.remove(i - 1)
            answer += 1
        elif i + 1 in reserveSet:
            reserveSet.remove(i + 1)
            answer += 1
            
    return answer