# 4-3
# 나의 답안
# 현재 나이트 좌표
night_now = input()

# 문자열 슬라이싱을 통해 좌표 행렬로 분리
x = night_now[0] # 알파벳 좌표
y = int(night_now[1]) # 숫자 좌표

# 이동 가능한 좌표 정의
move_type = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

count = 0
# 좌표 이동 수행
for move in move_type:
    nx = ord(x) + move[0]
    ny = y + move[1]
    
    # 정원을 벗어나는 경우 무시
    if (nx < ord('a') or nx > ord('h') or ny < 1 or ny > 8):
        continue
    
    count += 1

print(count)

# --------------------------------------------------------------------------------------------
# 예시 답안
# 현재 나이트 위치 입력받기
input_data = input()

# 행렬로 값 분리
row = int(input_data[1])
# 열 위치를 계산하기 쉽게 숫자로 변환
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]

# 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)