N = int(input())
lst = [list(input()) for _ in range(N)]
bucket = [0]*26
alpha = []

for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j] in alpha: continue
        alpha.append(lst[i][j])

len_alpha = len(alpha)
numbers = list(range(9,9-len_alpha,-1))

path = [0]*len_alpha

def calcu(path):
    num = 0
    for i in range(N):
        len_lsti = len(lst[i])
        for j in range(len_lsti):
            num += 10**(len_lsti-j-1)*(path[alpha.index(lst[i][j])])
    return num


Max = -21e8
used = [0]*len_alpha
def dfs(level):
    global Max
    if level == len_alpha:
        ret = calcu(path)
        if ret > Max:
            Max = ret
        return

    for i in range(len_alpha):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = numbers[i]
        dfs(level+1)
        used[i] = 0

dfs(0)
print(Max)