student = {
    'id': 1,
    'full_name': 'Nguyen Van A'
}
# print(student['id'])
# print(student.get('full_name', 'Tên mặc đinh'))

student['email'] = 'a@gmail.com'
student['full_name'] = 'Nguyen Thi B'

deleted_email = student.pop('email')
# del student['email']
print(student)

for key in student.keys():
    print(key)
    
for value in student.values():
    print(value)
    
for key, value in student.items():
    print(key, value)