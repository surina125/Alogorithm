def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    len_com = len(completion)
    for i in range(len_com):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
