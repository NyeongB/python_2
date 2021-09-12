'''
문제 : 막대기
날짜 : 21.09.12
'''

n = int(input())
arr = [64, 32, 16, 8, 4, 2, 1]
count = 0
for i in arr:
    if n >= i:
        count += 1
        n -= i
    
    if n == 0:
        break

print(count)