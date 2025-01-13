'''
Merge Sort (sắp xếp trộn)
'''

def merge_sort(arr):
    
    #? 1. Điều kiện gốc (cơ sở): khi mảng con chỉ có 1 phần tử -> không cần sắp xếp
    if len(arr) <= 1:
        return arr
        
    #? 2. Tìm index ở chính giữa và chia mảng ban đầu thành 2 mảng con bằng nhau
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    # print(f"Chia: {arr} -> {left_arr} và {right_arr}")

    #? 3. Đệ quy: sắp xếp lần lượt mảng bên trái và mảng bên phải
    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)
    
    #? 4. Ghép 2 mảng bên trái và bên phải lại để được mảng hoàn chỉnh (đã được sắp xếp thành công)
    merged_arr = merge(left_sorted, right_sorted)
    # print(f"Hợp nhất: {left_sorted} và {right_sorted} -> {merged_arr}")

    return merged_arr

def merge(left_arr, right_arr):
    
    #? Duyệt qua 2 mảng con và sắp xếp giá trị cho mảng trả về
    sorted_arr = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[i])
            j += 1

    #? Kiểm tra giá trị còn sót lại ở mảng bên trái
    while i < len(left_arr):
        sorted_arr.append(left_arr[i])
        i += 1

    #? Kiểm tra giá trị còn sót lại ở mảng bên phải
    while j < len(right_arr):
        sorted_arr.append(right_arr[j])
        j += 1
    
    #? Trả về mảng đã được sắp xếp
    return sorted_arr

numbers = [1, 15, 58, 65, 30, 23, 9, 12]

numbers.sort()

sorted = merge_sort(numbers)

