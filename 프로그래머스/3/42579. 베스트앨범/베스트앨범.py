def solution(genres, plays):
    ans = []
    total = {} 
    gen = {} 

    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        gen[genres[i]] = gen.get(genres[i], []) + [(plays[i], i)]

    genSort = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for (genre, totalPlay) in genSort:
        gen[genre] = sorted(gen[genre], key=lambda x: (-x[0], x[1]))
        ans += [idx for (play, idx) in gen[genre][:2]]

    return ans