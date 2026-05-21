# for i in range(5):
#     print(f'Vòng ngoài lần {i}')
#     for j in range(3):
#         print(f'Vòng trong lần {j}')
#     print()
    
# In ra hình vuông với dấu *
# có kích thước ngang, dọc được nhập vào

# 4,3
# ****
# ****
# ****
# width = int(input('Nhập vào chiều ngang: '))
# height = int(input('Nhập vào chiều rộng: '))
# In ra 1 hàng trong hình chữ nhật
# for i in range(height):
#     for j in range(width):
#         print('*', end='')
#     print()
    
# Nhập vào chiều cao hình tam giác
height = int(input('Nhập vào chiều cao tam giác: '))
# *
# **
# ***
# ****
# *****
for i in range(1, height + 1):
    for j in range(i):
        print('*', end='')
    print()
# *****
# ****
# ***
# **
# *
for i in range(1, height + 1):
    for j in range(height + 1 - i):
        print('*', end='')
    print()