'''
문제 : 소수 찾기
날짜 : 21.08.31
'''

from itertools import permutations as p

def isPrime(n):
    if n <=1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
    

def solution(numbers):
    answer = 0
    s = set()
    for i in range(1, len(numbers)+1):
        arr = list(p(map(int, numbers),i))
        for j in arr:
            s.add(int("".join(map(str,j))))
    
    for i in s:
        if isPrime(i):
            answer += 1
    return answer