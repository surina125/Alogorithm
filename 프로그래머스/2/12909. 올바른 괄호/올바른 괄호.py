def solution(s):
    answer = False
    stack = []
    for i in s:
        if stack and stack[-1] == "(":
            if i == ")":
                stack.pop()
            else :
                stack.append(i)
        else : 
            stack.append(i)
    
    if not stack :
        answer = True 
    return answer