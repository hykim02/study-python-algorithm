# 학생 수
# N = int(input())

# array = []
# for i in range(N):
#     data = input().split()
#     array.append((data[0], int(data[1])))

# result = sorted(array, key=lambda student: student[1])

# for i in result:
#     print(i[0], end=" ")


N = int(input())

ls = []
for i in range(N):
    data = input().split()
    ls.append((data[0], int(data[1])))

ls.sort(key=lambda student:student[1])

for i in ls:
    print(i[0], end=" ")
