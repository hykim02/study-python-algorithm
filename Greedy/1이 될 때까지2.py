# 3-6
n, k = map(int, input().split())
count = 0

while True:
    # n을 k로 나눌 수 있는 가장 가까운 배수로 만듦
    target = (n // k) * k
    # n을 target과 값이 같도록 하려면 (n-target)번 만큼 1씩 빼야함
    count += (n - target)
    n = target
    # n을 k로 나눌 수 없으면 반복문 종료    
    if n < k:
        break

    # n을 k로 나눔    
    count += 1
    n //= k
    
# 더 이상 나눌 수 없을 때, n이 1이 될 때까지 1씩 빼야함
# (n-1)번 횟수 만큼 1씩 빼면 1이 됨
count += (n-1)
print(count)