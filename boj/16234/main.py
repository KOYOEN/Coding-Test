from collections import deque

# 데이터 받아오기
N, L, R = map(int, input().split())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

union = [ [-1]* N for _ in range(N)]

def search(x, y, index):
    dq = deque() # BFS 정보
    united = [] # 결합한 나라 정보
    united.append((x, y))
    dq.append((x, y))
    summary = data[x][y]
    union[x][y] = index
    count = 1
    while dq:
        x, y = dq.popleft()
        # 4방향에 대해 접근
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(data[x][y] - data[nx][ny]) <= R:
                    united.append((nx, ny))
                    dq.append((nx, ny))
                    union[nx][ny] = index
                    summary += data[nx][ny]
                    count += 1

    for r, c in united:
        data[r][c] = summary // count

    return

answer = 0
while True:
    union = [[-1] * N for _ in range(N)]
    # union 이 되지 않은 곳에서 search를 시작
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                search(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난뒤
    if index == N * N:
        break
    answer += 1

print(answer)




