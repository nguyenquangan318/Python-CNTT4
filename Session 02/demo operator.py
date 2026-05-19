first_num = int(input('Nhập số thứ nhất: '))
second_num = int(input('Nhập số thứ hai: '))

print(f'Tổng của hai số là: {first_num + second_num}')
# Hiệu, tích, thương
print(f'Hiệu 2 số là: {first_num - second_num}')
print(f'Tích 2 số là: {first_num * second_num}')
print(f'Thương 2 số là {int(first_num / second_num)}')

print(first_num > second_num and first_num % 2 == 0)
print(first_num < second_num or second_num % 2 == 1)
print(not first_num > second_num)