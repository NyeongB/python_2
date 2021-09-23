'''
문제 : 문자열 뒤집기
날짜 : 21.09.23
'''

s = input()

count0 = 0 # 모두 0으로 만드는 비용
count1 = 0 # 모두 1로 만드는 비용

if s[0] == '0':
    count1 += 1
else:
    count0 += 1


for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))

