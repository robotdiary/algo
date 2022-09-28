# 다익스트라 연습
def dijkstra(n, x, adj, d):  # (nodes, start, arr, distance)
    # [1] 출발 노드 설정
    # 방문한 노드, 시작점 적어 놓기
    visited = [x]

    # [2] 최소 비용 테이블 초기화
    # distance에 우선 시작 노드에서 바로 가는 거리를 적어놓는다.
    # 바로 가는 길이 없는 경우 INF값(1000000)이 들어감
    for i in range(n + 1):
        d[i] = adj[x][i]  # 얕은 복사 방지

    # [5] 3, 4 반복
    for _ in range(n - 1):  # N개의 정점 중 출발을 제외한 정점 선택

        # [3] 방문하지 않은 노드 중 가장 짧은 노드 선택, 방문 처리
        w = 0  # 누가 될지 모르니 일단 0
        for i in range(1, n + 1):
            if i not in visited and d[i] < d[w]:  # 남은 노드 중 비용이 최소인 w
                w = i
        visited.append(w)

        # [3] 선택한 노드 - 인접 노드 간 가장 짧은 비용을 최소 비용 테이블에 업데이트
        for v in range(1, n + 1):
            if adj[w][v] < 1000000:  # 정점 i가 w에 인접이면
                d[v] = min(d[v], d[w] + adj[w][v])


T = int(input())
for tc in range(1, T + 1):
    nodes, edges, start = map(int, input().split())  # 노드 수, 간선 수, 시작점
    arr = [[1000000] * (nodes + 1) for _ in range(nodes + 1)]  # 2차원 배열
    # 자기 자신에게로 0의 거리
    for i in range(nodes + 1):
        arr[i][i] = 0
    # x노드에서 y노드로 c의 거리
    for _ in range(edges):
        x, y, c = map(int, input().split())
        arr[x][y] = c

    distance = [0] * (nodes + 1)
    dijkstra(nodes, start, arr, distance)
    print(distance)  # [1000000, 1, 0, 3, 7]