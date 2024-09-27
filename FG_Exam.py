
#Insertion Sort
#descending order
X = [1,2,21,33,46,65,12]
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1,len(arr)):
        if arr[min_idx] < arr[j]:
            min_idx=j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

#Selection sort
#ascending order
X = [1,2,21,33,46,65,12]
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1,len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx=j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]