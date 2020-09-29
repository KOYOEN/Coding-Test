from itertools import permutations

N = int(input())
num_array = list(map(int, input().split()))

yeon = ['+', '-', '*', '/']
yeon_num =  list(map(int, input().split()))

operator = ""
# string으로 들어가야하는 연산자 다넣기
for n, y in zip(yeon_num, yeon):
    operator += y * n

# operator의 순열 구하기
# 최대, 최소 순으로 값 구하기
answer = [-1e10, 1e10]

for op in permutations(operator):
    temp = num_array[0]
    for i in range(N-1):
        if op[i] == '+':
            temp += num_array[i+1]
        elif op[i] == '-':
            temp -= num_array[i+1] 
        elif op[i] == '*':
            temp *= num_array[i+1]
        elif op[i] == '/':
            if temp < 0 :
                t = temp
                t *= -1
                t //= num_array[i+1]
                temp = -1 * t
            else :
                temp //= num_array[i+1]

    if temp > answer[0] : 
        # 최대값인 경우
        answer[0] = temp
    if temp < answer[1] :
        # 최소값인 경우
        answer[1] = temp
    
for x in answer:
    print(x)
