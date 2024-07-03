#truy cập các mục danh sách, chỉ đến giá trị từ orange đến melon 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# thay đổi danh sách
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # thay banana bằng blackcurrant


#mở rộng danh sách 
thislist = ["abc","def","ghj"]
thistuple = ["123","456","789"]
thislist.extend(thistuple)
print(thislist)

#xoas list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #xoa banana khoi danh sach 


#xoa gia tri chi dinh 
thislist = ["abc","def","ghj"]
thislist.pop(2)
print(thislist) #xoa ghj

#danh sach vong lap 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #vong lap for
#
thislist = ["abc","def","ghj"]
i = 0 #biến đếm i
while i < len(thislist):  #điều kiện i nhỏ hơn độ dài của list
    print(thislist[i])
    i = i + 1 #vong lap while

#sắp xếp danh sách theo thứ tự bảng chữ cái
thislist = ["ông", "bà ", "cha", "mẹ ", "em "]
thislist.sort() #dùng sort()   #nếu dùng copy() thì sẽ tạo một bản sao danh sách cũ
print(thislist)


#