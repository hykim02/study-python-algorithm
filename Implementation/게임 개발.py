# 4-4
# 나의 답안
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 맵 생성(바다(1) or 육지(0))
game_map = []
for _ in range(n):
    map_row = list(map(int, input().split()))
    game_map.append(map_row)
    
# 칸의 방문 여부 확인을 위한 맵 생성
map_check = []
for _ in range(n): 
    map_check.append([0] * m)

map_check[a][b] = 1 # 현재 위치 방문 등록 

# 방향 정의(북, 동, 남, 서)
directions = [0, 1, 2, 3]
go_forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]
go_back = [(1,0), (0, -1), (-1, 0), (0, 1)]

turn_left = 0 # 회전 횟수 확인 변수 
count = 1 # 방문한 칸의 수(현재 위치 포함)

# 방향 탐색 및 좌표 이동
while(True):
    # 왼쪽 방향 탐색
    nd = d - 1
    if(nd == -1):
        nd = 3
    
    # 칸의 방문 여부 확인
    na = a + go_forward[nd][0]
    nb = b + go_forward[nd][1]
    
    # 가보지 않은 경우 & 육지인 경우
    if(map_check[na][nb] == 0 and game_map[na][nb] == 0):
        # 왼쪽 회전 수행
        d = nd
        # 한 칸 전진
        a, b = na, nb
        map_check[a][b] = 1
        count += 1
        turn_left = 0
        continue # 다음 탐색 수행 
    else:
        # 가본 경우 -> 회전만 수행
        d = nd
        turn_left += 1
        
    # 네 방향 모두 가본 칸이거나 바다로 되어 있는 경우
    if(turn_left == 4):
        # 한 칸 후진
        na = a + go_back[nd][0]
        nb = b + go_back[nd][1]
        
        # 후진한 칸이 바다인 경우 멈춤
        if(game_map[na][nb] == 1):
            break
        else: # 육지인 경우 후진 수행, 이미 가본 칸이므로 체크 X
            a = na
            b = nb
            turn_left = 0
        
print(count)

# --------------------------------------------------------------
# 예시 답안
# 맵 크기 입력받기
n, m = map(int, input().split())

# 방문 위치를 저장하기 위한 맵을 생성해 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 위치 & 방향 입력받기
x, y, direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 맵 상태 입력받기 (육지 or 바다)
map = []
for i in range(n):
    map.append(list(map(int, input().split())))

# 방향 정의(북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 한 칸 되돌아 갈 경우의 좌표 계산
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if map[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)


