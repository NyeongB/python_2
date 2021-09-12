'''
문제 : 수들의 합 2
날짜 : 21.09.12
'''

'''
10 5
1 2 3 4 2 5 3 1 1 2
'''

n, m = map(int,input().split())

arr = list(map(int,input().split()))

answer = 0

for idx, num in enumerate(arr):
    total = 0

    for i in range(idx,n):
        total += arr[i]

        if total >= m:
            break
    
    if total == m:
        answer += 1

print(answer)