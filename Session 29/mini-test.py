class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""
        
    def calculate_revenue(self):
        self.total_revenue = self.price * self.quantity_sold - self.discount
        if self.total_revenue < 0:
            self.total_revenue = 0
            
    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self):
        id = input("Nhập mã sản phẩm: ")
        name = input("Nhập tên sản phẩm: ")
        if name == "":
            print("Tên không hợp lệ")
            return
        # while True:
        #     name = input("Nhập tên sản phẩm: ")
        #     if name == "":
        #         print("Tên không hợp lệ")
        #     else:
        #         break
        price = float(input("Nhập giá sản phẩm: "))
        
        quantity_sold = int(input("Nhập số sản phẩm đã bán: "))
        discount = float(input("Nhập giá sản phẩm được giảm: "))
        new_product = Product(id, name, price, quantity_sold, discount)
        new_product.calculate_revenue()
        new_product.classify_revenue()
        self.products.append(new_product)
        print("Thêm sản phẩm thành công")
    
    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm trống")
            return
        print(f"{'Mã sản phẩm':<12}| {'Tên sản phẩm':<20}| {'Giá bán':<15}| {'Số lượng đã bán':<15}| {'Giảm giá':<15}| {'Tổng doanh thu':<15}| Loại doanh thu")
        for p in self.products:
            print(f"{p.id:<12}| {p.name:<20}| {p.price:<15}| {p.quantity_sold:<15}| {p.discount:<15}| {p.total_revenue:<15}| {p.revenue_type}")
    
    def update_product(self):
        update_id = input("Nhập mã sản phẩm muốn sửa")
        for p in self.products:
            if update_id == p.id:
                # cập nhật thông tin sản phẩm
                p.price = float(input("Nhập giá sản phẩm mới: "))
                p.quantity_sold = int(input("Nhập số sản phẩm đã bán mới: "))
                p.discount = float(input("Nhập giá sản phẩm được giảm mới: "))
                p.calculate_revenue()
                p.classify_revenue()
                print("Cập nhật thành công")
                return
        print("Sản phẩm không tồn tại")    
           
    def delete_product(self):
        delete_id = input("Nhập mã sản phẩm muốn xóa")
        for p in self.products:
            if delete_id == p.id:
                # xóa sản phẩm
                choice = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ")
                if choice == "Y":
                    self.products.remove(p)
                    print("Xóa thành công")
                elif choice == "N":
                    print("Hủy thao tác xóa")
                else:
                    print("Lựa chọn không hợp lệ")
                return
        print("Sản phẩm không tồn tại")  
    
    def search_product(self):
        search_result = []
        search_name = input("Nhập tên sản phẩm muốn tìm kiếm")
        for p in self.products:
            if search_name in p.name:
                print(f"{p.id:<12}| {p.name:<20}| {p.price:<15}| {p.quantity_sold:<15}| {p.discount:<15}| {p.total_revenue:<15}| {p.revenue_type}")
                search_result.append(p)
        if not search_result:
            print("Sản phẩm không tồn tại")      

def main():
    main = ProductManager()
    while True:
        choice = input('''================ MENU ================
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật sản phẩm
4. Xóa sản phẩm
5. Tìm kiếm sản phẩm
6. Thống kê doanh thu
7. Thoát
=====================================
Nhập lựa chọn của bạn:
''')
        match choice:
            case '1':
                main.show_all()
            case '2':
                main.add_product()
            case '7':
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ")
                
main()