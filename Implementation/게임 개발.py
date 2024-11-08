# 4-4
# 나의 답안
# 맵 크기 입력받기
n, m = map(int, input().split())

# 방문 여부 확인을 위한 맵 초기화
map_visit = []
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(0)
    map_visit.append(arr)

# 현재 위치 & 방향 입력받기
a, b, d = map(int, input().split())

# 맵 상태 입력받기 (육지 or 바다)
map_state = []
for i in range(N):
    state = list(map(int, input().split()))
    map.append(state)

# 방향 정의
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


