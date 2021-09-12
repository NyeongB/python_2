'''
문제 : 두 수의 합
날짜 : 21.09.12
'''

'''
9
5 12 7 10 9 1 2 3 11
13
'''

n = int(input())

arr = list(map(int,input().split()))

x = int(input())

answer = 0

arr.sort(reverse=True)

for idx, num in enumerate(arr):
    temp = x
    count = 0
    if temp > num:
        temp -= num
        for j in range(idx+1, n):
            
            if temp >= arr[j]:
                count +=1
                if count == 2:
                    break
                temp -= arr[j]
    if temp == 0:
        #print(str(num) +' '+ str(temp) + '!!')
        answer +=1


print(answer)    

'''
다시 맞았지만 시간이 많이 나옴
4828ms
'''