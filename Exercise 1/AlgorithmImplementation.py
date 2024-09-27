#Insertion Sort\

#[23,89, 7, 56, 44] – Implement the Bubble Sort Algorithm for the Dataset and
#sort the data into ascending order.
#Acending Order

arr1 = [23, 89, 7, 56, 44]
print("\nGive Data of Bubb"
      "le")
print(arr1)
for i in range(len(arr1)):
    for j in range(0, len(arr1) - i - 1):
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
print("Ascending Order Bubble Sort")
print(arr1)

#[12, 78, 91, 34, 62] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into ascending
#order.
#Acending Order

arr2 = [12, 78, 91, 34, 62]
print("\nGive Data of Insertion")
print(arr2)
for i in range(len(arr2)):
    key = arr2[i]
    j = i - 1
    while j >= 0 and key < arr2[j]:
        arr2[j + 1] = arr2[j]
        j -= 1
    arr2[j + 1] = key
print("Ascending Order Insertion Sort")
print(arr2)

#[5, 99, 48, 15, 67] – Implement the
#Selection Sort Algorithm for the Dataset and sort the data into descending
#order
#Descending Order

arr3 = [5, 99, 48, 15, 67]
print("\nGive Data of Selection")
print(arr3)
for i in range(len(arr3)):
    min_idx = i
    for j in range(i + 1, len(arr3)):
        if arr3[min_idx] < arr3[j]:
            min_idx = j
            # swapping the values from our array
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
print("Descending Order Selection Sort")

print(arr3)

#  [38, 82, 25, 74, 13] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into descending
#order.
#Descending Order

arr4 = [12, 78, 91, 34, 62]
print("\nGive Data of Insertion")
print(arr4)
for i in range(len(arr4)):
    key = arr4[i]
    j = i - 1
    while j >= 0 and key > arr4[j]:
        arr4[j + 1] = arr4[j]
        j -= 1
    arr4[j + 1] = key
print("Descending  Insertion Sort")
print(arr4)

#Copy all of the values from the
#second index and third index of the previous datasets into one
#dataset. After copying, sort the data into ascending order and descending
#order each order of the dataset is inserted into a separate list/array.
arr5 = [23, 44, 34, 62, 67, 48, 47, 38]
for i in range(len(arr5)):
    for j in range(0, len(arr5) - i - 1):
        if arr5[j] > arr5[j + 1]:
            arr5[j], arr5[j + 1] = arr5[j + 1], arr5[j]
print("\nAscending Order")
print(arr5)
arr5 = [23, 44, 34, 62, 67, 48, 47, 38]
for i in range(len(arr5)):
    for j in range(0, len(arr5) - i - 1):
        if arr5[j] < arr5[j + 1]:
            arr5[j], arr5[j + 1] = arr5[j + 1], arr5[j]
print("Descending Order")
print(arr5)

#Create a new list/array or values copying all of
#the values from item number 1 to 4. Implement the Selection
#ort Algorithm and sort the data into ascending order.

arr6 = [23,89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("\nGiven data of Selection Sort")
print(arr6)
for i in range(len(arr6)):
    min_idx = i
    for j in range(i + 1, len(arr6)):
        if arr6[min_idx] > arr6[j]:
            min_idx = j
            # swapping the values from our array
    arr6[i], arr6[min_idx] = arr6[min_idx], arr6[i]
print("Ascending Order in Selection Sort")
print(arr6)

#Print the even and odd values of the
#list/array created in item number 6.

arr7 = [23,89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("\nGiven data of Selection Sort")
print(arr7)
for i in range(len(arr7)):
    min_idx = i
    for j in range(i + 1, len(arr6)):
        if arr7[min_idx] > arr7[j]:
            min_idx = j
            # swapping the values from our array
    arr7[i], arr7[min_idx] = arr7[min_idx], arr7[i]
print("Ascending Order in Selection Sort")
print(arr7)

odd_numbers = [num for num in arr7 if num % 2 != 0]
even_numbers = [num for num in arr7 if num % 2 == 0]

print("\nOdd numbers:")
print(odd_numbers)
print("Even numbers:")
print(even_numbers)