grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)},
    {"id": "SV03", "name": "Trần Thị C", "info": (8.0, 7.0)},
    {"id": "SV04", "name": "Nguyễn Văn D", "info": (10.0, 9.0)}
]
grade_book.sort(key = lambda student: student['name'], reverse=True)
print(grade_book)
# Sắp xếp danh sách theo điểm trung bình
grade_book.sort(key = lambda s: (s['info'][0] + s['info'][1]) / 2)
print(grade_book)

# names = [student['name'] for student in grade_book]
# grade_book.sort()
# names.sort()
# sorted_names = sorted(names)
# print(names)
# print(sorted_names)

