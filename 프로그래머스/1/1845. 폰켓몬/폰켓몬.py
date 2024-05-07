from collections import Counter
def solution(nums):
    N = len(nums) / 2
    lst = Counter(nums)
    
    if N <= len(lst) :
        return N
    else:
        return len(lst)