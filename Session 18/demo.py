student_list = [{
    "id":"SV001",
    "full_name":"Nguyen Van A",
    "math": 8.5,
    "physics": 7.0,
    "chemis": 9.0,
    "avg": 8.17,
    "rank": "giỏi"
}]

def ranking(avg):
    if avg < 5:
        return 'Yếu'
    elif avg < 7:
        return 'TB'
    elif avg < 8:
        return 'Khá'
    else:
        return 'Giỏi'
    

def add_student():
    id = input('Nhập id sinh viên')
    full_name = input('Nhập tên sinh viên')
    math = float(input('Nhập điểm toán'))
    physics = float(input('Nhập điểm lý'))
    chemis = float(input('Nhập điểm hóa'))
    avg = (math + physics + chemis) / 3
    student_list.append({
        "id": id,
        "full_name": full_name,
        "math": math,
        "physics": physics,
        "chemis": chemis,
        "avg": avg,
        "rank": ranking(avg)
    })
    
def analyze_score():
    great_count = 0
    good_count = 0
    avg_count = 0
    weak_count = 0
    for student in student_list:
        if student['rank'] == 'Giỏi':
            great_count += 1
        elif student['rank'] == 'Khá':
            good_count += 1
        elif student["rank"] == 'TB':
            avg_count += 1
        else:
            weak_count += 1
    print(f'Giỏi: {great_count}, Khá: {good_count}, TB: {avg_count}, Yếu: {weak_count}')
    
while True:
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach")
    print("2. Them sinh vien")
    print("3. Cap nhat sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke hoc luc")
    print("7. Thoat")
    choice = input("Nhap lua chon: ")
    match choice:
        
        case '2':
            add_student()
        case '6':
            analyze_score()
        case '7':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')