# Vòng lặp while đến khi người dùng không tiếp tục chương trình
# Vòn lặp for bên trong để nhập thông tin và in từng nhân viên
choice = ""
while choice != "n":
    employee_number = int(input("Nhập số lượng nhân viên: "))
    for i in range(employee_number):
        
    choice = input('Tiếp tục chương trình? (y/n)')