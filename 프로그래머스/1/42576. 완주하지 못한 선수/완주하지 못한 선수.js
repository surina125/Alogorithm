function solution(participant, completion) {
    const par = participant.sort()
    const com = completion.sort()
    
    for (i = 0; i < com.length; i++) {
        if (par[i] !== com[i]) {
            return par[i]
        }
    }
    return par[par.length - 1];
}