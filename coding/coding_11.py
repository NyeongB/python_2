'''
문제 : 네트워크(BFS)
날짜 : 21.08.31
'''
from collections import deque

def bfs(i, c, v):
    q = deque()
    q.append(i)
    
    while q:
        temp = q.popleft()
        for j in range(len(c)):
            if j not in v and temp != j and c[temp][j] == 1:
                v.add(j)
                q.append(j)
                

def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            bfs(i, computers, visited)
            answer += 1
    
    return answer