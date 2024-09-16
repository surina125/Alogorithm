function solution(clothes) {
    let new_clothes = {}
    
    for (let i = 0; i < clothes.length; i++) {
        let type = clothes[i][1]
        if (!new_clothes[type]) {
            new_clothes[type] = []
        }
        new_clothes[type].push(clothes[i][0])
        }
            
    let answer = 1
    for (let type in new_clothes) {
        answer *= (new_clothes[type].length + 1)
    }
    return answer - 1
}