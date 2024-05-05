def solution(numbers, target):
    global answer
    answer = 0
    len_num = len(numbers)
    
    def dfs(level, Sum):
        global answer
        if level == len_num:
            if Sum == target:
                answer += 1
            return

        dfs(level+1, Sum+numbers[level])
        dfs(level+1, Sum-numbers[level])
    
    dfs(0,0)
    return answer