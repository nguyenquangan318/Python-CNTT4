math_score = float(input('Nhập điểm toán: '))
physic_score = float(input('Nhập điểm lý: '))
lit_score = float(input('Nhập điểm văn: '))
avg_score = (math_score + physic_score + lit_score) / 3
# nếu điểm TB > 5 thì in "Trên TB", nếu không thì in "Dưới TB"
if avg_score > 5:
    print('Trên TB')
else: 
    print('Dưới TB')

# Nếu 3 điểm trên 5 thì in ra qua môn
# Nếu có 1 trên 3 điểm dưới 5 thì in ra thi lại
# Nếu nhiều hơn 2 trên 3 điểm dưới 5 thì in ra học lại

count_under_five = 0
# Đếm số điểm nhỏ hơn 5, in ra theo số đó
if(math_score < 5):
    count_under_five +=1
if(physic_score < 5):
    count_under_five +=1
if(lit_score < 5):
    count_under_five +=1
if(count_under_five == 0):
    print('Qua môn')
elif(count_under_five == 1):
    print('Thi lại')
else: print('Học lại')

# Kết hợp điều kiện để in luôn
if(math_score > 5 and physic_score > 5 and lit_score > 5):
    print('Qua môn')
elif math_score < 5:
    if physic_score < 5 or lit_score < 5:
        print('Học lại')
    else:
        print('Thi lại')
elif physic_score < 5:
    if math_score < 5 or lit_score < 5:
        print('Học lại')
    else:
        print('Thi lại')
elif lit_score < 5:
    if math_score < 5 or physic_score < 5:
        print('Học lại')
    else:
        print('Thi lại')