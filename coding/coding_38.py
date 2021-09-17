'''
문제 : 오픈채팅방
날짜 : 21.09.17
'''

def solution(record):
    answer = []
    arr = []
    dic = {}
    for s in record:
        temp = s.split(" ")
        if temp[0] == "Enter":
            arr.append((temp[1],temp[0]))
            dic[temp[1]] = temp[2]
        elif temp[0] == "Change":
            dic[temp[1]] = temp[2]
        else:
            arr.append((temp[1],temp[0]))

    
    for s in arr:
        nick = dic[s[0]]
        
        if s[1] == 'Enter':
            nick += "님이 들어왔습니다."
        else:
            nick += "님이 나갔습니다."
        
        answer.append(nick)
    
    
    
    return answer