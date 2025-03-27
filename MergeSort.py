
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        mergeSort(L), mergeSort(R)
        i = j = 0
        for k in range(len(arr)):
            if j >= len(R) or (i < len(L) and L[i] < R[j]):
                arr[k], i = L[i], i + 1
            else:
                arr[k], j = R[j], j + 1

arr = [64, 34, 25, 12, 22, 11, 90]
mergeSort(arr)
print(arr)
