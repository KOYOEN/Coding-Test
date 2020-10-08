n = int(input())

T = [0] * (n+1)
P = [0] * (n+1)
for i in range(1, n+1):
    T[i] , P[i] = map(int, input().split())

array = [0] * 21
def solution():
    global T, P, n
    for i in range(1, n+1):
        # T는 기간 P는 돈
        temp = array[i] + P[i]
        for j in range(i+T[i], 21):
            if array[j] < temp :
                array[j] = temp
    return array[n+1]

print(solution())


    

