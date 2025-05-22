# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# A.sort() # 오름차순
# B.sort(reverse=True) # 내림차순 

# for i in range(K):
#     if A[i] < B[i]:
#         A[i], B[i] = B[i], A[i]
#     else:
#         break

# print(sum(A))



n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] >= b[i]:
        break
    else:
        a[i], b[i] = b[i], a[i]

print(sum(a))

