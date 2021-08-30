'''
문제 : 상호평가
날짜 : 21.08.30
'''
def grade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    
    for i in range(len(scores)):
        temp = []
        index = 0
        for j in range(len(scores[0])):
            
            temp.append(scores[j][i])
            
            if i == j :
                index = scores[j][i]
        
        if max(temp) == index or min(temp)== index:
            
            if temp.count(index) == 1:
                temp.remove(index)
        s = sum(temp)
        
        answer += grade(s/len(temp))
        
        
        
    
    return answer