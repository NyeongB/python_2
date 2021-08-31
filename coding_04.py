'''
문제 : 섬 연결하기
날짜 : 21.08.31
'''
rank = {}
parent = {}

def make_set(n) :
    for i in range(n):
        rank[i] = 0
        parent[i] = i
        
def find(v) :
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else :
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def solution(n, costs):
    answer = 0
    make_set(n)
    costs.sort(key=lambda x:x[2])
    
    for i,j,v in costs:
        if find(i) != find(j):
            union(i,j)
            answer += v
    
    
    return answer