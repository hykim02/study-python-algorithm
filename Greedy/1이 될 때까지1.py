# 3-5
# 나의 답안
n, k = map(int, input().split())
count = 0

while(n >= k):
    # n이 k로 나누어 떨어지는 경우
    if (n % k == 0):
        n //= k
        count += 1
    else: # 나누어 떨어지지 않는 경우
        count += (n % k) # 1을 빼야 하는 횟수
        n = ((n // k) * k)

if(n < k):
    count += (n-1) # n에서 (n-1)을 빼주면 1이 됨

print(count)

# -------------------------------------------------------------
# 예제 답안 1
n, k = map(int, input().split())
count = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        count += 1
    # K로 나누기
    n //= k
    count += 1

# N이 1이 될때까지 1씩 빼기
while n > 1:
    n -= 1
    count += 1

print(count)
