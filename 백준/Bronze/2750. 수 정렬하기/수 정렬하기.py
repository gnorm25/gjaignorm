N= int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



for i in range(N):
    print(arr[i])