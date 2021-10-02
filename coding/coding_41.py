'''
문제 : 예상 대진표
날짜 : 21.10.02
'''
def solution(n,a,b):
    answer = 0
    while a!=b:
        a= (a+1)//2
        b= (b+1)//2
        answer+=1
    return answer