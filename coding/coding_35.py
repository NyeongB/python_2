'''
문제 : 문자열 집합
날짜 : 21.09.14
'''

answer = 0

n, m = map(int,input().split())

s = set()

for _ in range(n):
    s.add(input())

for _ in range(m):
    if input() in s:
        answer += 1

print(answer)