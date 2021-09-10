'''
문제 : 약수의 개수와 덧셈
날짜 : 21.09.10
'''
def isEven(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count +=1
    
    if count % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0
    
    
    for num in range(left, right + 1):
        if isEven(num):
            answer += num
        else:
            answer -= num
    
    
    return answer