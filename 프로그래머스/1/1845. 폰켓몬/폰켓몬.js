function solution(nums) {
    a = new Set(nums).size
    b = ~~nums.length/2

    return a > b ? b : a
}