def solution(nums):
    num = len(set(nums))
    if num > (len(nums)//2):
        return (len(nums)//2)
    else:
        return num