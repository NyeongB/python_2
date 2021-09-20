'''
문제 : 괄호 회전하기
날짜 : 21.09.20
'''

def isTrue(s):
    st = []
    
    for i in s:
        if i =='(':
            st.append('(')
        elif i =='[':
            st.append('[')
        elif i =='{':
            st.append('{')
        elif len(st) ==0:
            return False
        else:
            if i == ')' and st[-1] =='(':
                st.pop()
            elif i == ']' and st[-1] =='[':
                st.pop()
            elif i == '}' and st[-1] =='{':
                st.pop()
    
    if len(st) == 0:
        return True
    else:
        return False
            
def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        if isTrue(s):
            answer += 1
        t = ''
        t = s[1:] + s[0]
        s = t
    
    return answer