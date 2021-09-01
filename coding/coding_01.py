'''
문제 : 요세푸스 문제
날짜 : 21.07.25
'''

from collections import deque

n, k = map(int, input().split())

q = [i for i in range(1, n+1)]

q = deque(q)
result = list()

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<', end='')
for i in range(n-1):
    print(result[i], end=', ')
print(result[-1],end='')
print('>')