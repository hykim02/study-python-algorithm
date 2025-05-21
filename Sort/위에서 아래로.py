N = int(input())

ls = []
for i in range(N):
    ls.append(int(input()))

# ls_sorted = sorted(ls, reverse=True)

# for i in ls_sorted:
#     print(i, end=" ")


ls.sort()
ls.reverse()

for i in ls:
    print(i, end=" ")