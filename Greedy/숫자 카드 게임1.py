# 3-3
# min 함수 이용
# 행열 개수 입력받기
import time
import psutil
import os

# 메모리 사용량 측정 함수
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # 메모리 사용량(MB 단위)

start_time = time.time()

n, m = map(int, input().split())

max_value = 0
# 행별로 숫자 입력받기
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 각 행별 최소값 찾기
    if (min_value > max_value):
        max_value = min_value
    else:
        continue

print(max_value)
print(f"Final memory usage: {memory_usage()} MB")

end_time = time.time()
print("time:", end_time - start_time)
# start_time = time.time()
# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)

# print(result)
# print(f"Final memory usage: {memory_usage()} MB")
# end_time = time.time()
# print("time:", end_time - start_time)
# start_time = time.time()
# n, m = map(int, input().split())

# min_list = []
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_list.append(min(data))

# print(max(min_list))
# end_time = time.time()
# print("time:", end_time - start_time)
# print(f"Final memory usage: {memory_usage()} MB")