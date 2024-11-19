# 4-2
# 나의답안
n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)

# ------------------------------------------------------------------
# 예시답안
h = int(input())
count = 0

# h + 1인 이유 -> h가 5이면 0시부터 5시까지 포함해야 하는데
# range 범위는 매개변수 본인은 포함하지 않기 때문
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)