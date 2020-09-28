from itertools import combinations

n, m = map(int, input().split())

array = [[0] * ( n + 1 )]
chicken = []
home = []
for row in range(1, n+1):
    array.append([0] + list(map(int, input().split())))
    for col, temp in enumerate(array[row]):
        if temp == 2:
            chicken.append((row, col))
        elif temp == 1:
            home.append((row, col))


answer = 987654321

for selected in combinations(range(len(chicken)), m):
    # 선택된 인덱스의 치킨집 거리를 체크
    city = 0
    for h_x, h_y in home:
        # 각 집에서 선택된 치킨집 까지의 거리를 측정
        street = 987654321 
        for idx in selected:
           c_x, c_y = chicken[idx]
           street = min(street, abs(h_x - c_x) + abs(h_y - c_y))
        city += street
    answer = min([answer, city])

print(answer)
            

    


