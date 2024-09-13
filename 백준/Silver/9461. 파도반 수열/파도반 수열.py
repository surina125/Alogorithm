arr = [0]*101
arr[1:11] = [1,1,1,2,2,3,4,5,7,9]

for i in range(10, 101):
    arr[i] = arr[i-2]+arr[i-3]

T = int(input())
for tc in range(T):
    n = int(input())
    print(arr[n])
