'''
문제 : 럭키 스트레이트
날짜 : 21.09.23
'''

n = input()

sum = 0

for i in range(len(n)//2):
    sum += int(n[i])
    
for i in range(len(n)//2, len(n)):
    sum -= int(n[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")