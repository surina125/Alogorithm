N = int(input())
arr = [list(map(str,input())) for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

def search():
    global Max
    # 행 탐색
    for n in range(N):
        cnt = 1
        for m in range(N-1):
            if arr[m][n] == arr[m+1][n]:
               cnt += 1
            else:
                cnt = 1
            if Max < cnt:
                Max = cnt
    #열 탐색
    for n in range(N):
        cnt = 1
        for m in range(N-1):
            if arr[n][m] == arr[n][m+1]:
               cnt += 1
            else:
                cnt = 1
            if Max < cnt:
                Max = cnt

Max = 1
search()
for i in range(N):
    for j in range(N):
        for k in range(4):
            dy = i+di[k]
            dx = j+dj[k]
            if dy<0 or dy>N-1 or dx<0 or dx>N-1: continue
            if arr[i][j] == arr[dy][dx]: continue
            # (i, j) <-> (dy, dx) 교환
            arr[i][j], arr[dy][dx] = arr[dy][dx], arr[i][j]
            search()
            arr[i][j], arr[dy][dx] = arr[dy][dx], arr[i][j]

print(Max)