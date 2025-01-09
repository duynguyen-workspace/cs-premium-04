'''
ĐỀ BÀI: 
- Tìm số lớn thứ nhì trong 1 mảng (chưa sắp xếp)

YÊU CẦU:
- Phân tích độ phức tạp thuật toán (time complexity và space complexity)

VÍ DỤ:
- Input: nums = [0, 2, 5, 10, 3, 7, 9] -> [0, 2, 3, 5, 7, 9, 10]
- Output: 9
'''

#TODO 1: Cách naive (thuần tuý)
nums = [2, 1, 4, 5, 10, 3, 7, 9, 20, 30] # 1 lần

# Cách thức giải bài tập: phương pháp 2 pointers

if (nums[0] > nums[1]): # Tổng cộng: 6 lần
    largest = nums[0] # nằm đầu mảng
    second_largest = nums[len(nums) - 1] # nằm cuối mảng
else:
    largest = nums[len(nums) - 1] 
    second_largest = nums[0]

for i in range(2, len(nums)):
    if (largest > nums[i]): 
        if (second_largest > nums[i]):
            continue
        else: 
            second_largest = nums[i]
    else:
        second_largest = largest
        largest = nums[i]


# for i in range(1, len(nums) - 1): # index 1 -> index 7
#     largest = nums[i] 
#     for j in range(i, len(nums)): 
#         if (largest < nums[i]): 
#             largest = nums[i] 

print("Số lớn nhất là:", largest) 
print("Số lớn nhì là:", second_largest) 


# Bài tập two-sums 

