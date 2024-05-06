from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def solution(maps):
    len_row = len(maps)
    len_col = len(maps[0])
    
    q = deque()
    used = [[0]*len_col for _ in range(len_row)]
    used[0][0] = 1
    q.append((0,0, 1))
    
    while q:
        nowy, nowx, level = q.popleft()

        for i in range(4):
            dy = nowy+di[i]
            dx = nowx+dj[i]

            if dy<0 or dy>len_row-1 or dx<0 or dx>len_col-1: continue
            if used[dy][dx] == 1: continue
            if maps[dy][dx] == 0: continue
            used[dy][dx] = 1
            q.append((dy, dx, level+1))

            if (dy, dx) == (len_row-1, len_col-1):
                return level+1
    return -1
    