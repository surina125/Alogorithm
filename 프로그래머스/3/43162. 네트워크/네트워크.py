from collections import deque

def solution(n, computers):
    answer = 0
    used = [0]*n

    for j in range(n):
        if used[j] == 1: continue

        answer += 1
        q = deque()
        used[j] = 1
        q.append(j)

        while q:                
            nowx = q.popleft()
            for i in range(n):
                if nowx == i: continue
                if computers[nowx][i] == 0: continue
                if used[i] == 1: continue
                q.append(i)
                used[i] = 1

    return answer