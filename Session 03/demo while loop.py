# Lặp đến khi nào người dùng nhập 'exit'
# user_input = ""
# while user_input != 'exit':
#     user_input = input('Nhập thao tác')
    
# In ra menu có định dạng và xử lý chức năng
# ---MENU---
# 1. Nhập tên
# Sau khi nhập thì in ra 'Xin chào ...'
# 2. Xóa tên
# Trước khi xóa thì in ra 'Tạm biệt ...'
# 3. Thoát

choice = 0
while choice != 3:
    print('---MENU---')
    print('1. Nhập tên')
    print('2. Xóa tên')
    print('3. Thoát')
    choice = int(input("Lựa chọn của bạn: "))
    match choice:
        case 1:
            user_name = input('Nhập tên của bạn')
            print(f'Xin chào {user_name}')
        case 2:
            print(f'Tạm biệt {user_name}')
            user_name = ""
        case 3:
            print('Thoát chương trình')
        case _:
            print('Lựa chọn không hợp lệ')