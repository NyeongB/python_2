'''
문제 : 두 용액
날짜 : 21.09.15
'''

'''
5
-2 4 -99 -1 98
'''

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = n-1
answer = abs(arr[start] + arr[end])

al = start
ar = end

while start < end:
    temp = arr[start] + arr[end]
    if abs(temp) < answer:
        al = start
        ar = end
        answer = abs(temp)
        if answer == 0:
            break
    
    if temp > 0:
        end -= 1
    else :
        start += 1

print(arr[al],arr[ar])

