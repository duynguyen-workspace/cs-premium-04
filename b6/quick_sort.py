'''
Quick Sort (sắp xếp nhanh)
'''
def quick_sort(arr):
    
    #? 1. Điều kiện gốc (cơ sở): khi mảng con chỉ có 1 phần tử -> giống merge sort
    if len(arr) <= 1:
        return arr
    
    #? 2. Chọn vị trí index làm pivot (điểm tựa) 
    pivot = arr[len(arr) // 2]
    
    #? 3. Lần lượt chia thành các mảng tương ứng với các mốc giá trị: bé hơn, bằng, và lớn hơn giá trị pivot
    left = [x for x in arr if x < pivot] # list comprehension
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    #? 4. Gộp các mảng con lại thành mảng chính
    return quick_sort(left) + middle + quick_sort(right)