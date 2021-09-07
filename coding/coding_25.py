'''
문제 : 숫자 문자열과 영단어
날짜 : 21.09.07
'''

def solution(s):
    answer = 0
    
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, eng in enumerate(arr):
        #print(eng)
        s = s.replace(eng,str(idx))
    
    answer = int(s)
    
    return answer