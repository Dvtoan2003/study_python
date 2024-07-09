# tính đa hình 
#trong python nó đề cập đến các phương thức/toán tử/hàm có cùng tên có thể thực thi trên nhiều đối tượng hoặc lớp 
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('drive')
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()



### đa hình qua phương thức chung
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Sử dụng đa hình qua phương thức sound()
def animal_sound(animal):
    print(animal.sound())

# Tạo đối tượng từ các lớp
dog = Dog()
cat = Cat()

# Gọi phương thức sound() mà không cần biết lớp cụ thể
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

### đa hình qua kế thừa 
class Animal:
   def speak(self):
      raise NotImplementedError("Subclass mmust implement abstract methood")

class Dog(Animal):
   def speak(self):
      return "gau gau"
class Cat(Animal):
   def speak(self):
      return"meo meo"
animals = [Dog(),Cat()]
for anima in animals :
   print(anima.speak())

### dda hinhf qua giao dien khong chinh thuwc 
class Car:
   def start(self):
      return "car is starting"
   
class Boat:
   def start(self):
      return"boat is starting"
# phương thức sử dụng giao diện không chính thức
def start_vehicle(vehicle):
   print(vehicle.start())
# tạo đối tượng từ các lớp khác nhau 
car = Car()
boat = Boat()
# gọi phơng thức start mà không cần biết lớp cụ thể 
start_vehicle(car)
start_vehicle(boat)
 