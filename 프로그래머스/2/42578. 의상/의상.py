def solution(clothes):
    clothes_dict = {}
    for clothe in clothes:
        clothes_dict[clothe[1]] = clothes_dict.get(clothe[1], 0) + 1
    
    answer = 1
    for value in clothes_dict.values():
        answer *= (value + 1)
    return answer -1
