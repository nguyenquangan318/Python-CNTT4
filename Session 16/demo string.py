grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]
name_list = grade_book[0]['name'].split()
full_name = " ".join(name_list)
print(f'Họ: {name_list[0]} Tên đệm: {name_list[1]} Tên: {name_list[2]}')
print(f'Họ và tên: {full_name}')

def print_student():
    print('---DANH SÁCH SINH VIÊN---')
    for student in grade_book:
        # print(f'{student['id']:<7} | {student['name']:<15} | {student['info'][0]:<10} | {student['info'][1]:<10}')
        # output = '{id:<7} | {name:<15} | {info[0]:<10} | {info[1]:<10}'.format_map(student)
        print('{id:<7} | {name:<15} | {info[0]:<10} | {info[1]:<10}'.format_map(student))
print_student()