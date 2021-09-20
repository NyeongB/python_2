'''
문제 : [3차] 파일명 정렬
날짜 : 21.09.20
'''

import functools

def condition(s):
    s = s.lower()
    idx_num = 0

    # 숫자 인덱스 찾기
    first = True
    temp = ''

    for idx,i in enumerate(s):
        if i.isdigit():
            if first:
                first = False
                idx_num = idx
            temp += i
        
    return (s[:idx_num], temp)


def comparator(a, b):
    
    aH, aN = condition(a) 
    bH, bN = condition(b)
    #print(aH, aN, bH, bN)
    
    if aH > bH:
        return 1
    elif aH < bH:
        return -1
    else:
        if int(aN) > int(bN):
            return 1
        elif int(aN) < int(bN):
            return -1
        else:
            return 0
    
    

def solution(files):
    answer = []
    
    files.sort(key=functools.cmp_to_key(comparator))
        
             
        
    
    return files