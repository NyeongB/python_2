'''
문제 : 이진 변환 반복하기
날짜 : 21.09.01
'''
def solution(s):
    
    b_count = 0 ## 변환횟수
    z_count = 0
    while s != '1':
        b_count += 1
        ## 0 제거
        temp = len(s) - s.count('0')
        z_count += s.count('0')
        s = format(temp,'b')
        
        
    answer = [b_count, z_count]    
    
    return answer