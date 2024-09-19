#แทรกค่าเข้าไปในตำแหน่งที่ถูกต้องของ list ย่อยที่ถูกจัดเรียงแล้ว
def insertion_sort(arr):
    for i in range(1 , len(arr)):
        key =arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
        
arr = [2,5,6,8,4,1]
print(insertion_sort(arr))