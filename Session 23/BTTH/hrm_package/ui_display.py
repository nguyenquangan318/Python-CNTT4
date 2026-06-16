from tabulate import tabulate

def display_records(atendances):
    table = []
    for atend in atendances:
        table.append({1: atend['id'], 2: atend['name'], 3: atend['times'][0], 4: atend['times'][1] if atend['times'][1] else '[Đang làm việc]'})
    display = tabulate(
        table, 
        headers={1: "Mã nhân viên", 2: "Tên Nhân Viên", 3: "Giờ vào", 4: "Giờ ra"},
        tablefmt="github"
    )
    print(display)