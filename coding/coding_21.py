'''
문제 : 여행경로
날짜 : 21.09.03
'''

temp = []

def dfs(start, tickets, visited,count,route):
    if len(tickets) == count:
        route.append(start[1])
        print(route)
        temp.append(route)
        return
    
    for idx, i in enumerate(tickets):
        if idx not in visited and start[1] == i[0]:
            
            route.append(i[0])
            visited.add(idx)
            count += 1
            
            dfs(i, tickets, visited,count,route)
            route.pop()
            count -=1
            visited.remove(idx)
    


def solution(tickets):
    answer = []
    
    # 출발지 선택
    start = [idx for idx,i in enumerate(tickets) if i[0]=="ICN"]
    
    print(start)
    
    for i in start:
        visited = set()
        visited.add(i)
        dfs(tickets[i], tickets, visited,1,['ICN'])
    
    print(temp)
    
    
    return answer