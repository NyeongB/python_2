'''
문제 : 배달
날짜 : 21.09.02
'''

from collections import deque

def solution(N, road, K):
    answer = 0
    arr = [[0]*(N+1) for _ in range(N+1)]
    d = [1e9]*(N+1)
    
    #최소값 보장
    for i,j,r in road:
        if arr[i][j] == 0:
            arr[j][i] = arr[i][j] = r
        else:
            arr[i][j] = arr[j][i] = min(r,arr[i][j])
    
    
    d[1] = 0
    q = deque()
    q.append(1)
    
    while q:
        x = q.popleft()
        
        for y in range(1,N+1):
            if arr[x][y] !=0:
                if d[y] > arr[x][y] + d[x] and d[x] + arr[x][y] <= K:
                    q.append(y)
                    d[y] = d[x] + arr[x][y]
                
    
    print(d)
    answer = len([i for i in d if i <= K])
    return answer