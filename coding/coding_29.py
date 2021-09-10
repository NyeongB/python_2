'''
문제 : 직업군 추천하기
날짜 : 21.09.10
'''
def solution(table, languages, preference):
    answer = ''
    
    total = []
    
    for s in table:
        temp = s.split(' ')
        sum = 0
        hs = {}
        for idx, t in enumerate(temp):
            hs[t] = idx
            
        
        for l, p in zip(languages, preference):
            if hs.get(l) != None:
                sum += (6 - hs.get(l)) * p
        
        total.append((temp[0], sum))
    
    total.sort(key=lambda x:x[1],reverse=True)
    
    # 점수가같으면 이름
    max = 0
    for i in total:
        if max < i[1]:
            max = i[1]
    last = []
    for i in total:
        if max == i[1]:
            last.append(i)
    
    last.sort()
    
    answer = last[0][0]
    
    return answer