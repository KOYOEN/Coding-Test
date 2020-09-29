import sys
sys.setrecursionlimit(10**9)

def dfs(v):
    if check[v]: # 방문한 적이 있는가?
        return
    if not check[prev_visit[v]]: # 사전에 방문해야하는 곳을 방문했는가?
        next_visit[prev_visit[v]] = v
        return
    check[v] = 1
    if next_visit[v]:
        dfs(next_visit[v])
    for i in graph[v]:
        dfs(i)

def solution(n, path, order):
    global N, graph, prev_visit, check, next_visit

    N = n
    start_room = 0
    num_of_room = 0

    # 그래프를 저장하는 배열
    graph = [[] for _ in range(N)]
    # 선방문해야 하는 방을 저장하는 배열, prev_visit[후방문방] = 선방문방
    prev_visit = [0 for _ in range(N)]
    # 그래프 노드 방문여부를 저장하는 배열
    check = [0 for _ in range(N)]
    #  후방문해야 하는 방을 저장하는 배열, next_visit[선방문방] = 후방문방
    next_visit = [0 for _ in range(N)]

    # 양 옆으로 길을 표시
   for room_A, room_B in path:
        graph[room_A].append(room_B)
        graph[room_B].append(room_A)

    # B에 방문하기 위해서는 A에 사전 방문해야한다.
    for room_A, room_B in order:
        prev_visit[room_B] = room_A

    # 0에 방문할 때 조건이 있다면 실패!
    if prev_visit[start_room]:
        return False

    check[start_room] = 1
    for i in graph[start_room]:
        dfs(i)

    for i in range(N):
        if check[i]:
            num_of_room += 1

    return True if num_of_room == N else False
 
