N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

candi = []

# (i, j)좌표가 십자가의 중심점이라 생각하고 십자가 찾기
# 문제 조건: 항상 두 개의 십자가를 놓을 수 있는 경우만 입력으로 주어진다.
for i in range(N):
    for j in range(M):
        if lst[i][j] == '.': continue
        Min = N
        # 상
        num = 0
        for k in range(1, N):
            if num > Min: break

            if 0 <= i-k < N and lst[i-k][j] == '#':
                num += 1
            else:
                if Min > num:
                    Min = num
                break
        # 하
        num = 0
        for k in range(1, N):
            if num > Min: break

            if 0 <= i+k < N and lst[i+k][j] == '#':
                num += 1
            else:
                if Min > num:
                    Min = num
                break
        # 좌
        num = 0
        for k in range(1, N):
            if num > Min: break

            if 0 <= j-k < M and lst[i][j-k] == '#':
                num += 1
            else:
                if Min > num:
                    Min = num
                break
        # 우
        num = 0
        for k in range(1, N):
            if num > Min: break

            if 0 <= j+k < M and lst[i][j+k] == '#':
                num += 1
            else:
                if Min > num:
                    Min = num
                break

        # 십자가 추가
        # 십자가 크기가 작은 것들도 다 그 좌표에서 들어갈 수 있음
        if Min > 0:
            for k in range(Min+1):
                candi.append([Min-k, (i, j)])
        else:
            candi.append([Min, (i, j)])

len_candi = len(candi)


# 십자가 안겹치게 두개 뽑기
Max = 1
for j in range(len_candi-1):
    biggest = j # 첫번째 십자가 인덱스 후보
    for i in range(j+1, len_candi):
        next_biggest = i # 두번째 십자가 인덱스 후보
        
        if (candi[biggest][0]*4+1)*(candi[next_biggest][0]*4+1) < Max: continue

        flag = 0
        for n in range(candi[biggest][0]+1):
            for m in range(candi[next_biggest][0]+1):
                # biggest십자가의 좌측
                if (candi[biggest][1][0], candi[biggest][1][1]+n) == (candi[next_biggest][1][0], candi[next_biggest][1][1]-m) or (
                    candi[biggest][1][0], candi[biggest][1][1] + n) == (candi[next_biggest][1][0], candi[next_biggest][1][1] + m) or (
                    candi[biggest][1][0], candi[biggest][1][1] + n) == (candi[next_biggest][1][0]-m, candi[next_biggest][1][1]) or (
                    candi[biggest][1][0], candi[biggest][1][1] + n) == (candi[next_biggest][1][0]+m, candi[next_biggest][1][1]):
                    flag = 1
                    break

                # biggest십자가의 우측
                if (candi[biggest][1][0], candi[biggest][1][1]-n) == (candi[next_biggest][1][0], candi[next_biggest][1][1]-m) or (
                    candi[biggest][1][0], candi[biggest][1][1] - n) == (candi[next_biggest][1][0], candi[next_biggest][1][1] + m) or (
                    candi[biggest][1][0], candi[biggest][1][1] - n) == (candi[next_biggest][1][0]-m, candi[next_biggest][1][1]) or (
                    candi[biggest][1][0], candi[biggest][1][1] - n) == (candi[next_biggest][1][0]+m, candi[next_biggest][1][1]):
                    flag = 1
                    break

                # biggest십자가의 상측
                if (candi[biggest][1][0]+n, candi[biggest][1][1]) == (candi[next_biggest][1][0], candi[next_biggest][1][1]-m) or (
                    candi[biggest][1][0] + n, candi[biggest][1][1]) == (candi[next_biggest][1][0], candi[next_biggest][1][1] + m) or (
                    candi[biggest][1][0] + n, candi[biggest][1][1]) == (candi[next_biggest][1][0]-m, candi[next_biggest][1][1]) or (
                    candi[biggest][1][0] + n, candi[biggest][1][1]) == (candi[next_biggest][1][0]+m, candi[next_biggest][1][1]):
                    flag = 1
                    break

                # biggest십자가의 하측
                if (candi[biggest][1][0]-n, candi[biggest][1][1]) == (candi[next_biggest][1][0], candi[next_biggest][1][1]-m) or (
                    candi[biggest][1][0]-n, candi[biggest][1][1]) == (candi[next_biggest][1][0], candi[next_biggest][1][1] + m) or (
                    candi[biggest][1][0]-n, candi[biggest][1][1]) == (candi[next_biggest][1][0]-m, candi[next_biggest][1][1]) or (
                    candi[biggest][1][0]-n, candi[biggest][1][1]) == (candi[next_biggest][1][0]+m, candi[next_biggest][1][1]):
                    flag = 1
                    break

            if flag == 1: break

        else:
            two_cross_max = (candi[biggest][0]*4+1)*(candi[next_biggest][0]*4+1)

            if Max < two_cross_max:
                Max = two_cross_max

print(Max)




