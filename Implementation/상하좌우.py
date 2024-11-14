# 4-1
# 나의 답안
# 공간 크기 입력받기
n = int(input())
move_plans = list(input().split())

# 이동 방향 정의 
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 출발 위치는 항상 (1, 1)
x, y = 1, 1

# 이동 계획 수행
for move_plan in move_plans:
    idx = move_types.index(move_plan) # 문자 인덱스 찾기
    nx = x + dx[idx]
    ny = y + dy[idx]

    # 정사각형을 벗어나는지 확인
    if (nx >= 1 and nx <= n and ny >= 1 and ny <= n):
        x = nx
        y = ny
    else:
        continue

print(x, y)

# ----------------------------------------------------------------
# 예제 답안
n = int(input())
x, y = 1, 1
plans = input().split() # 이동 방향이 리스트로 생성됨

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)