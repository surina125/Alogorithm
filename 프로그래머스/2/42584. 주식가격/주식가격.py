from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue :
        price = queue.popleft()
        time = 0
        for q in queue :
            time += 1
            if price > q :
                break
        answer.append(time)
        
    return answer