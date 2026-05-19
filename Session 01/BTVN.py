import random

date_of_birth = int(input('Nhập năm sinh'))

patient_id = 'BN' + str(date_of_birth) + str(random.randint(100, 999))
print(patient_id)