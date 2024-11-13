# 3-1
# 나의 답안
# 거스름돈 입력받기
n = int(input("거스름돈:"))
count = 0
coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    rest = n % coin
    n = rest 

print(count)

# --------------------------------------------------------------------
# 예제 답안
n = int(input("거스름돈:"))
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    
print(count)
