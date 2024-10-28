# 3-2
# n, m, k를 공백으로 구분해 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분해 입력받기
data = list(map(int, input().split()))

# 리스트 정렬(라이브러리 사용)
data.sort()
first = data[-1] # 가장 큰 수
second = data[-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m // (k+1)) * k
count += m % (k+1)

result = 0 
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)