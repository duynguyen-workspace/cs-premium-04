import time
import random

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from merge_sort import merge
from quick_sort import quick_sort

'''
Hàm đo thời gian thực thi của các thuật toán sắp xếp

    @param: 
        - sort_function: thuật toán sắp xếp được sử dụng
        - arr: mảng cần được sắp xếp
'''

def measure_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort or sort_function == merge_sort:
        sorted_arr = sort_function(arr)
    else:
        sort_function(arr)
        
    end_time = time.time()
    return end_time - start_time

#? Tạo 1 mảng random các giá trị
array_size = 100000 
random_list = [random.randint(0, 100000) for _ in range(array_size)] # 0 -> 999999

#? Copy giá trị mảng random vào từng mảng riêng để thực hiện thuật toán sắp xếp
bubble_list = random_list.copy()
selection_list = random_list.copy()
insertion_list = random_list.copy()
merge_list = random_list.copy()
quick_list = random_list.copy()

#? So sánh tốc độ từng loại
print("Sắp xếp mảng có 100,000 phần tử:")
print(f"Bubble Sort: {measure_time(bubble_sort, bubble_list):.6f}s")
print(f"Selection Sort: {measure_time(selection_sort, selection_list):.6f}s")
print(f"Insertion Sort: {measure_time(insertion_sort, insertion_list):.6f}s")
print(f"Merge Sort: {measure_time(merge_sort, merge_list):.6f}s")
print(f"Quick Sort: {measure_time(quick_sort, quick_list):.6f}s")

# VD1: [4, 8, 12, 50, 32]

# VD2: [9, 15, 58, 65, 23, 11]

# VD3: [68, 31, 70, 22, 99, 120, 16, 25, 58, 82]