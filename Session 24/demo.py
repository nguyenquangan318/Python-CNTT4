class Student:
    school = "PTIT"
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.__phone = phone

    def say_hello(self):
        print(f'Xin chào, tôi là {self.name}')
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, new_phone):
        self.__phone = new_phone
    
    @staticmethod
    def check_phone(phone):
        return len(phone) >= 10

        
        
# student1 = Student(1, "Nguyễn Văn B", '0123456789')
# student1.say_hello()
# print(student1.name)
# print(Student.school)

# phone = input('Nhập số điện thoại sinh viên')
# if(Student.check_phone(phone)):
#     new_student = Student(1, "Nguyễn Văn A", phone)
# Student.test()

new_student = Student(1, "Nguyễn Văn A", "0123456789")
print(new_student.phone)
new_student.phone = '0987654321'
print(new_student.phone)