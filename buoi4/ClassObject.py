# class là một khuân mẫu để tạo ra các đối tượng
# nó định nghĩa các đặc điểm( thuộc tính ) và hành vi(phương thức) của các đối tượng 
class Dog:
    species = "Canix  familari" # thuoc tinh class
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def description(self):
        return f"{self.name} is {self.species} and {self.age} tuoi "
    def speak(self, sound):
        return f"{self.name} speak {sound}"
    
# object laf một phiên bản cụ thể của lớp 
# mỗi đối tượng  có các thuộc tính riêng và thực hiện các hành đỘng được định nghĩa trong lớp
dog1 = Dog("abc", 2)
dog2 = Dog("lucy", 3)
print(dog1.description())
print(dog2.speak("meo meo"))

# khoi tao class
class Student:
    id = ''
    name = ''
    # phuong thuc (method)
    def __init__(self, id, name):
        print('function add student')
        self.id = id
        self.name = name
    
    def show(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")

# su dung class (using class)
s = Student('001', 'toan')
s.show()

