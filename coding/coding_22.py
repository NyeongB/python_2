'''
문제 : 좋은단어
날짜 : 21.09.04
'''

n = int(input())
arr = []

arr = [input() for _ in range(n)]
count = 0

for temp in arr:
    stack = []
    for i in list(temp):
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0:
        count += 1



print(count)