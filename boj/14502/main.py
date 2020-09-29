from itertools import combinations
import copy

n, m = map(int, input().split())

# 연구소는 빈칸, 벽, 바이러스가 존재
blank = []
wall = []
virus = []
array = []
for r in range(n):
    temp = list(map(int, input().split()))
    for c, t in enumerate(temp):
        if t == 0: # 빈칸인 경우
            blank.append((r, c))
        elif t == 1: # 벽인 경우
            wall.append((r, c))
        else :
            virus.append((r,c))
    array.append(temp)

def spread(location, t_array):
    x, y = location
    t_array[x][y] = 2

    # 4 방면으로 뿌리기
    if 0 < x and t_array[x-1][y] == 0:
        spread((x-1, y), t_array)
    if x < n - 1 and t_array[x+1][y] == 0 :
        spread((x+1, y), t_array)
    if 0 < y and t_array[x][y-1] == 0:
        spread((x, y-1), t_array)
    if y <m - 1 and t_array[x][y+1] == 0:
        spread((x, y+1), t_array)

answer = 0
for selected in list(combinations(blank, 3)):
    # 3가지 점을 선택해서 벽을 세운다.
    t_array = copy.deepcopy(array)
    for (x, y) in selected:
        t_array[x][y] = 1
    # virus를 퍼트린다.
    for location in virus:
        spread(location, t_array)
    # 0으로 안전지대만을 체크한다.
    score = 0
    for i in range(n):
        for j in range(m):
            if t_array[i][j] == 0:
                score += 1

    answer = max(answer, score)
print(answer) 
