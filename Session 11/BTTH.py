product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    choice = input('''===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
Lựa chọn của bạn: ''')
    match choice:
        case '1':
            if(product_list == []):
                print('Danh sách sản phẩm hiện đang trống.')
                continue
            for i,product in enumerate(product_list):
                print(f'{i+1}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Số lượng: {product['quantity']}')
        case '2':
            # Nhập và validate mã sản phẩm
            id_input = input('nhập mã sản phẩm: ')
            name_input = input('nhập tên sản phẩm: ')
            price_input = input('nhập giá sản phẩm: ')
            quantity_input = input('nhập số lượng sản phẩm: ')

            # Nhập và validate giá và số lượng
            # Tạo dictionary mới và thêm vào list
        case '5':
            print('Thoát chương trình')
            break
        case _:
            print('Lựa chọn không hợp lệ')