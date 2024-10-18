def solution(s):
    cnt = 0
    q = list(s)
    for i in q:
        if cnt < 0:
            return False
        if i == '(':
           cnt += 1
        else:
            cnt -= 1
    if cnt != 0: return False        
    return True