def solution(phone_book):
    answer = True
    phone_book.sort()
    N = len(phone_book)
    for i in range(N-1):
        M = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:M]:
            answer = False 
            break
    return answer