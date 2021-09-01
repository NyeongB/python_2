'''
문제 : 더 맵게
날짜 : 21.08.31
'''
import heapq as h

def solution(scoville, K):
    answer = 0
    
    h.heapify(scoville)
    while True:
        tempA = h.heappop(scoville)
        
        if tempA < K and len(scoville) == 0:
            answer = -1
            break
        
        if tempA >= K:
            break
        
        tempB = h.heappop(scoville)
        h.heappush(scoville, tempA + tempB*2)
        answer +=1
    return answer