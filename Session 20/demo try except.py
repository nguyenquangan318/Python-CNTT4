def divide(number):
    print(10 / number)

try:
    number = float(input('Nhập số: '))
    divide(number)
except ValueError:
    print('Gặp lỗi value error')
except:
    print('Lỗi')
else:
    print('code trong try không bị lỗi')