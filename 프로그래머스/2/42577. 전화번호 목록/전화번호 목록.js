function solution(phone_book) {
    const ph = phone_book.sort()
    for (i = 0; i < ph.length - 1; i++) {
        num = 0
        for (j = 0; j < ph[i].length; j++) {
            if (ph[i][j] === ph[i+1][j]) {
                num += 1
            }
        if (num === ph[i].length) {
            return false
        }}
    }
    return true
}