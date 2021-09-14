'''
문제 : 타깃 넘버
날짜 : 21.09.14
'''

answer = 0
def dfs(numbers,idx,target,total):
    global answer
    
    if len(numbers) == idx:
        if target == total:
            answer += 1
        return
    
    dfs(numbers,idx+1,target,total + numbers[idx])
    dfs(numbers,idx+1,target,total + -1 * numbers[idx])

def solution(numbers, target):
    
    dfs(numbers, 0, target, 0)
    return answer