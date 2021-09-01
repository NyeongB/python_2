'''
문제 : 조이스틱
날짜 : 21.09.01
'''
def solution(name):
    
    cost = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    
    answer = 0
    
    idx = 0
    
    while True:
        answer += cost[idx]
        cost[idx] = 0
        
        if sum(cost) == 0:
            break
        
        ## 좌,우 판단 0인 지점이 안나올때까지
        left, right = 1, 1
        while cost[idx - left] == 0:
            left += 1
        while cost[idx + right] == 0:
            right += 1            
    
        answer += left if left < right else right
        idx += -left if left < right else right
    
    return answer