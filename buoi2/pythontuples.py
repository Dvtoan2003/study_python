# Đoạn mã kiểm tra số lượng phần tử trong tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # 3 phần tử 

# Đoạn mã truy cập các phần tử từ chỉ số 2 đến chỉ số 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  

# Đoạn mã chuyển tuple thành list, thêm phần tử, rồi chuyển lại thành tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) 

#k thể xoá tupl, chỉ có cách chuyển tuple thành list rồi xoá rồi chuyển lại từ list thành tuple 
thistuple = ("toan" ,"hien")
y = list(thistuple)
y.remove("toan") # dùng remove
thistuple = tuple(y)
print(thistuple)

# gán giá trị cho biến 
family = ("toan","hien","vinh","chieu")
(trai, gai, bo, me) = family
print(trai)
print(gai)
print(bo)
print(me)

#vòng lặp for tuple
family = ("toan","hien","vinh","chieu")
for item in family: #vòng lặp for
    print(item)


students_scores = (("Alice", 85), ("Bob", 90), ("Charlie", 78)) #tuple chứa các tuple con
for name, score in students_scores:  # Dùng vòng lặp for và unspacking để in từng tuple con
    print(f"Student: {name}, Score: {score}")


colors = ("red", "green", "blue", "yellow")
for index, color in enumerate(colors):  # Dùng vòng lặp for với enumerate để lấy chỉ số và giá trị
    print(f"Index: {index}, Color: {color}")

#vòng lặp while tuple
my_tuple = (10, 20, 30, 40, 50)
index = 0 # Khởi tạo biến chỉ số
while index < len(my_tuple):  # điều kiện biến đếm phải nhỏ hơn số phần tử
    print(my_tuple[index])
    index += 1





