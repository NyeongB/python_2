'''
문제 : N개의 최소공배수
날짜 : 21.09.02
'''
import heapq

def solution(arr):
    answer = 0
    heapq.heapify(arr)
    
    while len(arr) != 1:
        b = heapq.heappop(arr)
        a = heapq.heappop(arr)
        gdc = a * b
        # 유클리드 호제법
        while b != 0:
            temp = b
            b = a % b
            a = temp
        heapq.heappush(arr,gdc/a)
    
        
    answer = heapq.heappop(arr)
    return answer