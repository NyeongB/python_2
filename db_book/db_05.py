'''
문제 : 문자열 재정렬
날짜 : 21.09.23
'''

'''
K1KA5CB7 -> ABCKK13

A0C0D0B0 -> ABCD


'''

s = input()

arr = []
sum = 0
for i in list(s):
    if 65<= int(ord(i)) <= 90:
        arr.append(i)
    else:
        sum += int(i)

arr.sort()

if sum !=0:
    arr.append(str(sum))

print(''.join(arr))