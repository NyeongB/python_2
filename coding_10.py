'''
문제 : 네트워크
날짜 : 21.08.31
'''

def dfs(v, computers, visited):
    visited.add(v)
    
    for i in range(len(computers)):
        if v!= i and computers[v][i] == 1 and i not in visited:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    visited = set()
    
    for i in range(n):
        if i not in visited:
            dfs(i, computers, visited)
            answer += 1
    
    return answer