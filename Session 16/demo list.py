grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"id": "SV03", "name": "Trần Thị C", "info": (8.0, 7.0)},
    {"id": "SV04", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]

# Tạo ra danh sách chỉ chứa tên sinh viên có điểm trung bình >= 8

# Sử dụng vòng lặp bình thường
names = []
# for student in grade_book:
#     names.append(student['name'])
# print(names)
for student in grade_book:
    avg = (student['info'][0] + student['info'][1]) / 2
    if(avg >= 8):
        names.append(student['name'])
print(names)


# Sử dụng phương thức
# Cú pháp: method_name(function, iterable)
# names = list(map(lambda student: student['name'], grade_book))
names = list(filter(lambda student: (student['info'][0] + student['info'][1]) / 2 >= 8, grade_book))
print(names)

# Sử dụng list comprehension
# Cú pháp:  [expression for item in iterable if condition]
names = [student['name'] for student in grade_book if (student['info'][0] + student['info'][1]) / 2 >= 8]
print(names)
