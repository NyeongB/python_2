'''
문제 : 양
날짜 : 21.10.03
'''


'''
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
'''

from collections import deque

d = [(0,1), (0,-1), (1,0), (-1,0)]

r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

visited = set()

total_o = 0
total_v = 0

q = deque()



for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and (i,j) not in visited:

            if arr[i][j] == 'o':
                total_o +=1
            elif arr[i][j] == 'v':
                total_v += 1


            q.append((i,j))
            all = [] # 양, 늑대 임시 
            visited.add((i, j))
            all.append(arr[i][j])
            while q:
                x, y = q.popleft()
                
                for idx in range(4):
                    dx = x + d[idx][0]
                    dy = y + d[idx][1]
                    
                    if 0<= dx < r and 0 <= dy < c and (dx, dy) not in visited:
                        if arr[dx][dy] != '#':
                            if arr[dx][dy] == 'o':
                                total_o +=1
                            elif arr[dx][dy] == 'v':
                                total_v += 1
                            q.append((dx,dy))
                            visited.add((dx,dy))
                            all.append(arr[dx][dy])

            temp_o = all.count('o')
            temp_v = all.count('v')

            if temp_o <= temp_v:
                total_o -= temp_o
            else:
                total_v -= temp_v
            


print(total_o, total_v)
