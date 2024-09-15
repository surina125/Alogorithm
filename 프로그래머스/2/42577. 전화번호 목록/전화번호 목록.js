function solution(phone_book) {
    const ph = phone_book.sort()
    for (i = 0; i < ph.length - 1; i++) {
        if (ph[i+1].startsWith(ph[i])) {
            return false
        }
    }
    return true
}