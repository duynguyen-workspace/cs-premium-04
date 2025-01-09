'''
ĐỆ QUY
'''

def demo_dequy(num):
    print(f"Demo đệ quy: {num}")
    
    if num == 10:
        return "kết thúc đệ quy"
    
    demo_dequy(num + 1)
    
    print(f"kết thúc đệ quy bước số: {num}")
    
# demo_dequy(1)

#? Tính giai thừa -> O(n)
def factorial(n):
    # Điều kiện gốc: n == 1
    if n == 1:
        return 1
    
    
    return n * factorial(n - 1)

#  print(f"Kết quả giai thừa {factorial(5)}")

# n * factorial(n - 1) * factorial(n - 2) * ... factorial(1)

# factorial(2) = 2

# factorial(3) = n * factorial(n - 1) * factorial(n - 2)
#              = 3 * factorial(2) * factorial(1) = 3 * 2 * 1 = 6

# factorial(4)

#? Dãy số Fibonancci

# 1, 2, 3, 5, 8, ..., n

'''
    @param: n - vị trí số trong dãy fibonacci
    VD: n = 3 -> 3, n = 5 -> 8
    
    @note:
    - Cách tính: số nth tiếp theo sẽ là -> nth = (n - 1) + (n - 2)
    VD: 5th = (5 - 1) + (5 - 2) = 4th + 3th = 5 + 3 = 8
'''
def fibonacci(n): # Độ phức tạp: 2^n
    # Điều kiện gốc: n = 1 hoặc n = 2
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return fibonacci(n - 1) + fibonacci(n - 2)

index = int(input("Nhập vào vị trí trong dãy Fibonacci: "))
result = fibonacci(index)

print(f"Giá trị tại vị trí {index} là: {result}")