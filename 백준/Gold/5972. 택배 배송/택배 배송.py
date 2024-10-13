import sys
import heapq

input = sys.stdin.readline  # 빠른 입력
INF = int(21e8)  # 무한대 값 설정

# 입력 처리
n, m = map(int, input().split())  # n: 헛간 수, m: 길의 수
graph = [[] for _ in range(n)]  # 그래프 인접 리스트

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1  # 0-index로 맞추기
    b -= 1
    graph[a].append((c, b))  # a -> b 비용 c
    graph[b].append((c, a))  # b -> a 비용 c (양방향)

# 다익스트라 알고리즘
def dijkstra(start):
    dist = [INF] * n  # 시작점에서 각 정점까지의 최단 거리
    dist[start] = 0  # 시작점까지의 거리는 0
    pq = [(0, start)]  # (비용, 정점) 형태로 우선순위 큐 초기화

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # 이미 처리된 노드는 무시
        if current_cost > dist[current_node]:
            continue

        # 인접 노드 탐색
        for next_cost, next_node in graph[current_node]:
            total_cost = current_cost + next_cost

            # 더 적은 비용으로 도달할 수 있다면 갱신
            if total_cost < dist[next_node]:
                dist[next_node] = total_cost
                heapq.heappush(pq, (total_cost, next_node))

    return dist

# 헛간 1에서 N으로 가는 최단 거리 계산
result = dijkstra(0)  # 헛간 1은 0번 인덱스
print(result[n - 1])  # 헛간 N은 n-1번 인덱스
