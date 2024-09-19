#การเรียงข้อมูลด้วยการสลับที่หากพบมีค่าน้อยกว่า
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                

arr = [64, 34, 25, 12, 22, 11, 90] ##O(n²)): If the array is in reverse order, Bubble Sort will take the maximum number of comparisons and swaps.
arr = [1,2,3,4,5,6,7,8,9,10] #Best Case (O(n)): If the array is already sorted, Bubble Sort can finish in one pass.



bubble_sort(arr)

print("Sorted array is:", arr)
