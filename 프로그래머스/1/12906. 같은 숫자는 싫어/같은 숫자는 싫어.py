def solution(arr):
    stack = []
    for num in arr:
        if stack and stack[-1] == num :
            pass
        else : stack.append(num)
    return stack