#ค้นหาใน list ที่ถูกจัดเรียงแล้วด้วยการแบ่งครึ่ง list ในแต่ละครั้ง


def binary_search(arr , target):
    low , high = 0 , len(arr) - 1
    
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return arr[middle]
        elif arr[middle] < target:
            low = middle +1
        else:
            high = middle -1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#target = 5 # The best case for binary search happens when the target element is located at the middle of the list on the first attempt
#target = 1 or 10 The worst case occurs when the target element is either not in the list or is located at one of the extreme ends (either the very first or the very last position).
target = 6
print(binary_search(arr , target))

    
        

