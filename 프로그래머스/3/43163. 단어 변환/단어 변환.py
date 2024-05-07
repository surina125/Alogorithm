def solution(begin, target, words):
    global Min
    Min = 21e8
    
    if target not in words:
        return 0
    
    idx = words.index(target)
    
    len_words = len(words)
    len_word = len(words[0])
    
    used = [0]*len_words
    
    def dfs(level, target):
        global Min
        if used[idx] == 1:
            if Min > level:
                Min = level
            return
        if level == len_words:
            return
        
        for i in range(len_words):
            if used[i] == 1: continue
            for j in range(len_word):
                if target[:j] == words[i][:j] and target[j+1:] == words[i][j+1:] and target[j] != words[i][j]:
                    used[i] = 1
                    dfs(level+1, words[i])
                    used[i] = 0
                    
    dfs(0, begin)
    if Min == 21e8:
        return 0
    
    return Min