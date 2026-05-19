#  in từ 0 - 5
# for i in range(6):
#     print(f'Lần lặp thứ {i}')
    
# In các số chẵn từ 0 - 10
for i in range(0, 11, 2):
    print(f'Lần lặp thứ {i}')
    
# trong các số từ 1 - 20
# Nếu chia hết cho 3 thì in 'Số ... chia hết cho 3'
# Nếu chia hết cho 5 thì in 'Số ... chia hết cho 5'
# Nếu chia hết cho cả 3 và 5 thì in 'Số ... chia hết cho cả 3 và 5'
for i in range(3,21):
    if i % 5 == 0 and i % 3 == 0:
        print(f'Số {i} chia hết cho cả 3 và 5')
    elif i % 3 == 0:
        print(f'Số {i} chia hết cho 3')
    elif i % 5 == 0:
        print(f'Số {i} chia hết cho 5')