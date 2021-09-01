'''
문제 : 게임 맵 최단거리
날짜 : 21.09.01
'''

from collections import deque

def solution(maps):
    
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0<= nx < len(maps) and 0<= ny < len(maps[0]) and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
            
    answer = maps[len(maps)-1][len(maps[0])-1]
    return answer if answer >1 else -1