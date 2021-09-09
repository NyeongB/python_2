'''
문제 : 소수 만들기
날짜 : 21.09.09
'''
from itertools import combinations

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        #print(num, i)
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    arr = list(sum(i) for i in list(combinations(nums,3)))
    
    
    for num in arr:
        if isPrime(num):
            answer += 1

    return answer