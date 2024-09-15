def solution(phone_book):
    phone_book.sort()
    
    len_ph = len(phone_book)
    for i in range(len_ph-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True