def solution(clothes):
    len_clothes = len(clothes)
    types = []
    for i in range(len_clothes):
        if clothes[i][1] not in types:
            types.append(clothes[i][1])
    len_types = len(types)
    new_clothes = [[] for _ in range(len_types)]
    for i in range(len_clothes):
        new_clothes[types.index(clothes[i][1])].append(clothes[i][0])
    
    answer = 1
    for i in range(len_types):
        answer *= (len(new_clothes[i])+1)
    return answer-1