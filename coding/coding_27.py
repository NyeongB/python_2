'''
문제 : 복서 정렬하기
날짜 : 21.09.09
'''
import functools

def comparator(a,b):
    if a[0] < b[0]:
        return 1
    elif a[0] > b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] < b[1]:
            return 1
        elif a[1] > b[1]:
            return -1
        elif a[1] == b[1]:
            if a[2] < b[2]:
                return 1
            elif a[2] > b[2]:
                return -1
            elif a[2] == b[2]:
                if a[3] < b[3]:
                    return 1
                else:
                    return -1

def solution(weights, head2head):
    answer = []
    idx = 0
    l = len(weights)
    arr = []
    for w, h in zip(weights, head2head):
        temp = []
        
        # 승률, 몸무게많은 이긴수, 자기몸무게, 작은번호수
        if (l-list(h).count('N')) == 0:
            cnd1 = 0
        else: 
            cnd1 = (list(h).count('W') / (l-list(h).count('N')) * 100)
        temp.append(cnd1)
        count = 0
        for i, num in enumerate(list(h)):
            
            if num == 'W':
                if w < weights[i]:
                    count +=1
        
        temp.append(count)
        temp.append(w)
        temp.append(l-idx)
        temp.append(idx+1)
        
        arr.append(temp)
        idx += 1
    arr.sort(key=functools.cmp_to_key(comparator))
    
    print(arr)
    
    for i in arr:
        answer.append(i[4])
    
    return answer