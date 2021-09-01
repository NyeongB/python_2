'''
문제 : 가장 큰 수
날짜 : 21.08.31
'''

import functools

def comparator(a,b):
    num1 = int(str(a)+str(b))
    num2 = int(str(b)+str(a))
    
    if num2 > num1:
        return 1
    else:
        return -1

def solution(numbers):
    answer = ''
    
    numbers.sort(key=functools.cmp_to_key(comparator))
    
    answer = "".join(map(str,numbers))
    
    return str(int(answer))