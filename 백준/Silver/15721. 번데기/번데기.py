persons = int(input())
tar_num = int(input())
tar = int(input())

t = 0 # tar 나온 횟수
per = 0 # 사람 번호
flag = 0 # 종료 조건

for i in range(2, 10001):
    if flag == 1: break

    sen = [0,1,0,1]+[0]*i+[1]*i
    len_sen = len(sen)

    for j in range(len_sen):
        # 원 모양으로 사람들이 둥글게 앉았기 때문에 한바뀌 돌면 번호 리셋
        if per == persons:
            per = 0

        if sen[j] == tar:
            t += 1

        # 종료 조건
        if t == tar_num:
            flag = 1
            break
        
        # 다음차례 사람
        per += 1

print(per)