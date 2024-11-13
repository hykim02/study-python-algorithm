# 3-3
# 나의 답안
# 행, 열 개수 입력받기
n, m = map(int, input().split())

# 숫자 입력받기 -> 2차원 배열 생성 동시에 최솟값 추출 
cards = []
min_list = []
for i in range(n):
    row_card = list(map(int, input().split()))
    cards.append(row_card)
    min_list.append(min(row_card))

print(max(min_list)) # 최솟값들 중에 가장 큰 수 출력 

# -----------------------------------------------------------------
# 예제 답안 1
# min 함수를 이용한 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value) # 두 개의 값 중에 더 큰 값 반환

print(result)