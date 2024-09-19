#ค้นหาข้อมูลทั้งหมดใน list โดยวน loop ผ่านข้อมูลทั้งหมด  

import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return f'data {target} not found'

arr = [5, 6, 7, 2]

#target = 5 ฺBest case if the target is first element 
#target = 2 or another not present  , worst case if the target is at the end of list or not present
target = 2

print(linear_search(arr, target))

