def bfs(start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = deque([start])
    visitedBFS[start[0]][start[1]] = True
    cnt = 1

    while Q:
        x, y = Q.popleft()

        for dx,dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if matrix[nx][ny] == 1 and not visitedBFS[nx][ny]:
                    Q.append((nx,ny))
                    visitedBFS[nx][ny] = True
                    cnt += 1
    bfsCnt.append(cnt)

####
import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())

    matrix = [[0]*N for _ in range(M)]

    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        matrix[x][y] = 1

    visitedBFS = [[False]*N for _ in range(M)]
    bfsCnt = []

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1 and not visitedBFS[i][j]:
                bfs((i,j))

    print(min(bfsCnt))