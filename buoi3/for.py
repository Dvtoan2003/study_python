family = ["toan", "vinh", "chieu","hien"]
for x in family:
  print(x)

#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #khi vòng lặp đến banana  thì dừng
#
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": #không in ra banana nữa 
    continue
  print(x)

#hàm ranger() mặc định bắt đầu từ 0 và kết thúc ở số chỉ định
for x in range(9):
  print(x)

# vòng lồng nhau 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break