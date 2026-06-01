branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True:
    choice = input('''===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): ''')
    match choice:
        case '1':
            print(f'{'Tên cơ sở':<30}| {'Doanh thu':<15}| {'Trạng thái':<10}')
            print('-'*65)
            for i in range(len(branch_names)):
                print(f'{branch_names[i]:<30}| {daily_revenues[i]:<15}| {'Đạt' if target_achieved[i] else 'Không đạt':<10}')
            print('-'*65)
            print(f'=> TỔNG DOANH THU TOÀN VÙNG: {sum(daily_revenues)}')
        case '2':
            max_index = daily_revenues.index(max(daily_revenues))
            min_index = daily_revenues.index(min(daily_revenues))
            print(f'''- Cơ sở co doanh thu CAO NHAT: {branch_names[max_index]} ({daily_revenues[max_index]})
- Cơ sở co doanh thu THẤP NHẤT: {branch_names[min_index]} ({daily_revenues[min_index]})''')
        # case '3':
        case '4':
            print('Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!')
            break
        case _:
            print('[Loi] Lua chon khong hop le, vui long nhap lai so tu 1 den 4!')
            