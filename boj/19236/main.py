INF = 1e9

array = []
for _ in range(4):
    temp = list(map(int, input().split()))
    arr = []
    for i in range(4):
        arr.append([temp[2*i], temp[2*i+1]])
    array.append(arr)


dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def move():
    for x in range(1, 17):
        for i in range(4):
            for j in range(4):
                n, d = array[i][j]
                if n != x:
                    continue
                nx = i + dx[d]
                ny = j + dy[d]
                while 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or array[nx][ny][0]< 1:
                    d = (d + 1) % 9
                    if d == 0 :
                        d += 1
                    nx = i + dx[d]
                    ny = j + dy[d]

                array[i][j][1] = d
                array[i][j], array[nx][ny] = array[nx][ny], array[i][j]

answer = 0

def dfs(now_x, now_y, point, array):
    global answer
    # 물고기를 잡아먹음, 먹은자리는 0, d
    point += array[now_x][now_y][0]
    array[now_x][now_y][0] = 0

    if point > answer:
        answer = point
    
    # 물고기 이동
    move()
    d = array[now_x][now_y][1]
    for i in range(1, 4):
        nx = now_x + dx[d] * i
        ny = now_y + dy[d] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and array[nx][ny][0] != 0:
            dfs(nx, ny, point, array)


dfs(0, 0, 0, array)
print(answer)





