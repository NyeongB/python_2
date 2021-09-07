'''
문제 : 음양 더하기
날짜 : 21.09.07
'''

def solution(absolutes, signs):
    answer = 0
    
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else :
            answer -= num
    
    return answer