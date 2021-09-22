'''
문제 : 곱하기 혹은 더하기
날짜 : 21.09.22
'''

'''
02984

567
'''

n = input()

answer = int(n[0])

for i in range(1, len(n)):
    temp = int(n[i])

    if temp <= 1 or answer <= 1:
        answer += temp
    else:
        answer *= temp

print(answer)
    