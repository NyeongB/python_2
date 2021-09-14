'''
문제 : 등수 매기기
날짜 : 21.09.14
'''

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()
answer = 0
for i in range(1, n+1):
    answer += abs(arr[i-1] - i)

print(answer)