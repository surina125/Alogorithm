function solution(clothes) {
    const len_clothes = clothes.length
    let types = []
    for (i = 0; i < len_clothes; i++) {
        if (!(types.includes(clothes[i][1]))) {
            types.push(clothes[i][1])
        }
    }
    
    const len_types = types.length
    let new_clothes = Array.from({ length: len_types }, () => [])
    
    for (i = 0; i < len_clothes; i++) {
        new_clothes[types.indexOf(clothes[i][1])].push(clothes[i][0])
    }
    
    answer = 1
    for (i = 0; i < len_types; i++) {
        answer *= (new_clothes[i].length + 1)
    }
    return answer - 1
}