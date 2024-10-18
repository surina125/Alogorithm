def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse = True)
    
    len_a = len(a)
    Sum = 0
    for i in range(len_a):
        Sum += a[i]*b[i]
        
    return Sum
    