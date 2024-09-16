def solution(array, commands):
    len_commands = len(commands)
    answer = []
    for i in range(len_commands):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return answer