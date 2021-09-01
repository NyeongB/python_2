'''
문제 : 부족한 금액 계산하기
날짜 : 21.08.26
'''
def solution(price, money, count):
    answer = -1
    temp = 0
    for i in range(count):
        temp += price*(i+1)
    if(money >= temp):
        answer = 0
    else:
        answer = temp - money
    return answer