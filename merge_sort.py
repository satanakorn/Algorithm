#แบ่งครึ่ง list แล้วทำการเรียงในแต่ละครึ่งก่อนผสมกลับ
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        L =arr[:middle]
        R = arr[middle:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i]  < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print('Sorted array is:', merge_sort(arr))
