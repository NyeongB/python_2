'''
문제 : 다음 큰 숫자
날짜 : 21.09.02
'''

def solution(n):
    answer = 0
    c = format(n,'b').count('1')
    for i in range(n+1, 1000001):
        c_netx = format(i, 'b').count('1')
        if c == c_netx:
            answer = i
            break
    
    return answer