students = ['Ngân', 'Đạt', 'Huy', 'Diệp']
# Thêm vào cuối
students.append('Việt')
# Thêm vào vị trí
students.insert(10, 'An')
# Nối thêm 1 danh sách khác
students.extend(['1','2','3'])

# Xóa theo giá trị
students.remove('Việt')
# Xóa theo chỉ mục
students.pop(0)
# Xóa theo danh sách
del students[0:2:1]

