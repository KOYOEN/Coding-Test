n = int(input())
array = [0] * 1001
array[1] = 1
array[2] = 2

for x in range(3, n+1):
    array[x] = (array[x-1] + array[x-2]) % 10007
    
print(array[n])
