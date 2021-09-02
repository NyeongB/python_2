'''
문제 : 행렬 테두리 회전하기
날짜 : 21.09.01
'''


def solution(rows, columns, queries):
    answer = []
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    board = [[j + columns*i for j in range(1,columns+1) ] for i in range(rows)]
    
    for command in queries:
        idx = 0
        x1,y1,x2,y2 = command
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        x,y = x1,y1
        
        temp = board[x][y]
        Min = temp
        while idx < 4:
            dx = d[idx][0] + x
            dy = d[idx][1] + y
            
            if x1<= dx <=x2 and y1<=dy<=y2:
                Min = min(Min,board[dx][dy])
                board[x][y] = board[dx][dy]
                x,y = dx,dy
            else:
                idx += 1
        board[x][y+1] = temp
        
        answer.append(Min)
        
    
    
    return answer