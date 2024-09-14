function solution(nums) {
    num = [... new Set(nums)]
    
    a = num.length
    b = ~~nums.length/2

    if (a > b) {
        return b
    } else {
        return a
    }
}