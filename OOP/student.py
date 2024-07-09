class Student(): # student có attribute là id , name
    count=0
    #method
    def __init__(self, id , name): # function khoi tao object
        
        self.id=id 
        self.name=name
        Student.count+=1
    
    def get_id(self):
        return self.id
    def set_name(self, name):
        self.name=name
    def get_name(self):
        return self.name
    def show(self):
        print(f'ID:{self.id}')
        print(f'Name:{self.name}')
#use class
s = Student('BH00136','Van Toan')
s = Student('BH00137','Do Van Toan')
print(Student.count)

