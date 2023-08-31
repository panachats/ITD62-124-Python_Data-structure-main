def insertion(arr):
    for i in range(len(arr)):
        for x in range(i+1,len(arr)):
            if arr[i] > arr[x]:
                temp = arr[x]
                arr[x] = arr[i]
                arr[i] = temp
    print(arr)
arr = [1,55,8,99,3]

print(arr)
#arr = [(int(input('Enter you : '))) for y in range(n)]
insertion(arr)

