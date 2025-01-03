'''
ĐỀ BÀI: 
- Tìm số lớn nhất trong 1 mảng (chưa sắp xếp)

YÊU CẦU:
- Phân tích độ phức tạp thuật toán (time complexity và space complexity)

VÍ DỤ:
- Input: nums = [0, 2, 5, 10, 3, 7, 9] -> [0, 2, 3, 5, 7, 9, 10]
- Output: 10
'''

#TODO 1: Cách naive (thuần tuý)
nums = [4, 1, 2, 5, 10, 3, 7, 9, 20] # 1 lần
largest = nums[0] # 1 lần

for i in range(1, len(nums)): # n - 1 lần
    if (largest < nums[i]): # n - 1 lần
        largest = nums[i] # n - 1 lần 
        
nums.remove(20)

for i in range(1, len(nums)): # n - 1 lần
    if (largest < nums[i]): # n - 1 lần
        largest = nums[i] # n - 1 lần 

print("Số lớn nhất là:", largest) # 1 lần


#* F(N) = 3(n-1) + 3 lần -> Time Complexity: O(N) -> OLog(N), O(1)

#? Best Case: khi số lớn nhất nằm ở vị trí đầu tiên hoặc cuối cùng của mảng -> O(N)
#? Average Case: số lớn nhất nằm ở giữa mảng -> O(N)
#? Worst Case: khi số lớn nhất nằm ở cuối mảng -> O(N)

#TODO 2: Cách gần hay hơn
# Sắp xếp mảng -> Merge Sort / Quick Sort -> Time Complexity: O(NLogN)