import sys
sys.setrecursionlimit(10**8)

n = int(input())

data = [ [0] * n for _ in range(n)]

shark = (-1, -1)
fish = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
            # 아기상어 위치
            shark = (i ,j)
            continue
        elif temp[j] > 0:
            # 물고기 위치
            fish.append((i, j))
        data[i][j] = temp[j]
# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 987654321
# 물고기 DFS
def DFS(now, size, eat, time):
    # now는 위치, size는 상어크기, eat은 현재크기에서 몇마리 먹었는가?
    global data, fish, n, answer
    # 잡아먹을 수 있는 물고기가 존재하는가?
    check = False
    for lo in fish:
        x, y = lo
        if data[x][y] < size:
            check = True
            break

    if check == False:
        if answer > time:
            answer = time
        return

    x, y = now
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] < size:
            if data[nx][ny] == 0:
                # 물고기가 없는 경우
                DFS((nx, ny), size, eat, time+1)
                continue
            # 물고기가 있는경우
            temp = data[nx][ny]
            eat += 1
            if eat >= size:
                size += 1
                eat = 0
            data[nx][ny] = 0
            fish.remove((nx, ny))
            DFS((nx, ny), size, eat, time+1)
            data[nx][ny] = temp
            fish.append((nx, ny))


DFS(shark, 2, 0, 0)
print(answer)









