from collections import deque

n = int(input())
box = [list(input()) for _ in range(n)]

# 처음 위치 B랑 E 중심점 찾기
# 가로의 형태면 0, 세로의 형태면 1 추가 저장

# 가로의 형태
for i in range(n):
    for j in range(1, n-1):
        if box[i][j] == 'B' and box[i][j-1] == box[i][j] and box[i][j] == box[i][j+1]:
            st = ([i, j], 0)
            box[i][j-1], box[i][j], box[i][j+1] = '0', '0', '0'
        if box[i][j] == 'E' and box[i][j-1] == box[i][j] and box[i][j] == box[i][j+1]:
            ed = ([i, j], 0)
            box[i][j-1], box[i][j], box[i][j+1] = '0', '0', '0'
# 세로의 형태
for j in range(n):
    for i in range(1, n - 1):
        if box[i][j] == 'B' and box[i-1][j] == box[i][j] and box[i+1][j] == box[i][j]:
            st = ([i, j], 1)
            box[i-1][j], box[i][j], box[i+1][j] = '0', '0', '0'
        if box[i][j] == 'E' and box[i-1][j] == box[i][j] and box[i+1][j] == box[i][j]:
            ed = ([i, j], 1)
            box[i - 1][j], box[i][j], box[i + 1][j] = '0', '0', '0'

# 해당 인덱스의 값이 나무의 중심점이 그 위치까지 이동하기 까지 최소 동작 횟수
bucket = [[[21e8, 21e8] for __ in range(n)] for _ in range(n)]
# 예를 들어 bucket[0][1][0] : (0,1) 중심점까지 세로 형태(0)의 나무가 이동하기 까지 최소 동작 횟수

# 출발지 최소 동작횟수 0으로 셋팅
bucket[st[0][0]][st[0][1]][st[1]] = 0

# 방문한 곳 체크 배열
used = [[[0, 0] for __ in range(n)] for _ in range(n)]
used[st[0][0]][st[0][1]][st[1]] = 1

# 방향 배열 -> 여기서는 중심점 이동만 생각하고, 중심점 이동 후 경우 나누어 회전 추가
di = [0,0,1,-1]
dj = [1,-1,0,0]

q = deque()
q.append((st[0], st[1], 0))
flag = 0

while q:
    if flag == 1: break

    posi, shape, level = q.popleft()
    nowy, nowx = posi


    for i in range(4):
        dy = nowy+di[i]
        dx = nowx+dj[i]
        # (dy, dx)는 이동할 중심점 위치
        if shape == 0 and (dy < 0 or dy > n-1 or dx <= 0 or dx >= n-1): continue
        if shape == 1 and (dy <= 0 or dy >= n - 1 or dx < 0 or dx > n - 1): continue


        # 회전 안하고 이동
        if used[dy][dx][shape] == 0 and bucket[dy][dx][shape] > level+1 and box[dy][dx] == '0':
            if shape == 0:
                if box[dy][dx-1] == '0' and box[dy][dx+1] == '0':
                    used[dy][dx][shape] = 1
                    bucket[dy][dx][shape] = level+1
                    q.append(([dy, dx], 0, level+1))
                    if (dy, dx, 0) == (ed[0][0], ed[0][1], ed[1]):
                        flag = 1
                        break

            else:
                if box[dy-1][dx] == '0' and box[dy+1][dx] == '0':
                    used[dy][dx][shape] = 1
                    bucket[dy][dx][shape] = level+1
                    q.append(([dy, dx], 1, level+1))
                    if (dy, dx, 1) == (ed[0][0], ed[0][1], ed[1]):
                        flag = 1
                        break

        # 회전
        if used[nowy][nowx][(shape+1)%2] == 0 and bucket[nowy][nowx][(shape+1)%2] > level+1:
            if 0 < nowy < n-1 and 0 < nowx < n-1:
                if box[nowy-1][nowx-1:nowx+2] == ['0', '0', '0'] and box[nowy][nowx-1:nowx+2] == ['0', '0', '0'] and box[nowy+1][nowx-1:nowx+2] == ['0', '0', '0']:
                    used[nowy][nowx][(shape+1)%2] = 1
                    bucket[nowy][nowx][(shape + 1) % 2] = level+1
                    q.append(([nowy, nowx], (shape + 1) % 2, level+1))
                    if (nowy, nowx, (shape + 1) % 2) == (ed[0][0], ed[0][1], ed[1]):
                        flag = 1
                        break


if used[ed[0][0]][ed[0][1]][ed[1]] == 1:
    print(bucket[ed[0][0]][ed[0][1]][ed[1]])
else:
    print(0)
