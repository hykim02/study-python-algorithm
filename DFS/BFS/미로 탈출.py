from collections import deque
n, m = map(int, input().split())

miro = []
for i in range(n):
    miro.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    return miro[n-1][-1]

print(bfs(0, 0))