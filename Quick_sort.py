#เลือกค่า pivot แล้วแบ่งlistออกเป็นส่วนที่มากกว่าและน้อยกว่า

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", quick_sort(arr))
