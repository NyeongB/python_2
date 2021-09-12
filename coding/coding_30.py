'''
문제 : 배열 합치기
날짜 : 21.09.12
'''

a, b = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
 
answer = []
idxA = 0
idxB = 0


while idxA < a and idxB < b:
    if arrA[idxA] < arrB[idxB]:
        answer.append(arrA[idxA])
        idxA += 1
    else : 
        answer.append(arrB[idxB])
        idxB += 1

while idxA < a:
    answer.append(arrA[idxA])
    idxA += 1

while idxB < b:
    answer.append(arrB[idxB])
    idxB += 1    


print(' '.join(map(str,answer)))