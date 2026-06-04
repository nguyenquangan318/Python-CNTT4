grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book):
    print('Xem bảng điểm học sinh')
    print(f'{'Mã SV':<5} | {'Tên Học Sinh':<20} | {'Điểm Toán':<10} | {'Điểm Anh':<10} | {'ĐTB'}')
    for student in book:
        math_score, english_score = student['info']
        avg = (math_score + english_score) / 2
        print(f'{student['id']:<5} | {student['name']:<20} | {(math_score):<10} | {(english_score):<10} | {(avg)}')

def add_student(book):
    stu_id_input = input("nhậ mã học sinh:")
    for v in book:
        if stu_id_input == v["id"]:
            print("đã có ma học sinh trên, vui lòng nhập mã khác")
            return 
    stu_name_input = input("Nhập tên học sinh:")
    match_input = float(input("Nhập điểm toán:"))
    english_input = float(input("Nhập điểm anh:"))
    book.append({
        "id": stu_id_input, 
        "name": stu_name_input, 
        "info": (match_input, english_input)
    })
    print("đã thêm thành công !")
    
while True:
    choice = input('''=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5): ''')
    match choice:
        case '1':
            display_grades(grade_book)
        case '2':
            add_student(grade_book)
        case '5':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')