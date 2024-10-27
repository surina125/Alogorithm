import sys

input = sys.stdin.read().splitlines()
N = int(input[0])
liquids = list(map(int, input[1].split()))

liquids.sort()

closest_sum = float('inf')
ans = []

# 첫 번째 용액을 고정하고 나머지 두 용액을 투 포인터로 탐색
for i in range(N - 2):
    # 이미 최적 값에 도달한 경우 남은 탐색을 건너뛰도록 최적화
    if i > 0 and liquids[i] == liquids[i - 1]:  # 중복된 값 건너뛰기
        continue

    left, right = i + 1, N - 1
    while left < right:
        current_sum = liquids[i] + liquids[left] + liquids[right]
        
        # 현재 합이 0에 더 가깝다면 갱신
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            ans = [liquids[i], liquids[left], liquids[right]]
        
        # 최적 값(0)에 도달했다면 조기 종료
        if current_sum == 0:
            break

        # 포인터 이동
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    
    # 최적 값이 이미 0이라면 더 이상의 탐색 필요 없음
    if closest_sum == 0:
        break

print(*ans)
