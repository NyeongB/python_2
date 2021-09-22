'''
문제 : 모험가 길드
날짜 : 21.09.22
'''

'''
5
2 3 1 2 2
'''

answer = 0

n = int(input())

arr = list(map(int,input().split()))
arr.sort()

count = 0
for i in arr:
    count +=1
    if count >=i:
        count = 0
        answer +=1

print(answer)

'''
answer = 0

n = int(input())

arr = list(map(int,input().split()))
h = {}
for i in arr:
    if h.get(i,0) == 0:
        h[i] = 1
    else:
        h[i] = h.get(i) + 1


for k, v in h.items():
    if k <= v:
        answer += 1

print(answer)
'''