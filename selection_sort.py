#เลือกค่าน้อยสุดแล้วแล้วสลับมาไว้ด้านหน้า
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr 

arr = [5, 4, 7, 5]
print(selection_sort(arr)) 
