age = 25
if age < 18:
    print("Bạn là vị thành niên.")
elif age < 60:
    print("Bạn là người lớn.")
else:
    print("Bạn là người cao tuổi.")



# kiểm tra số chẵn hay lẻ
number = 30
if number > 0: #điều kiện number lớn hơn 0
    if number % 2 == 0: # điều kiện number chia hết cho 2
        print(f"{number} là số dương và là số chẵn.")
    else:
        print(f"{number} là số dương và là số lẻ.")
else:
    print(f"{number} là số âm hoặc bằng không.")


# kiểm tra xem giá trị của biến 
room_type = "Vip"
rooms_available = {"Single": 5, "Double": 0, "Vip": 2, "Normar": 1} # dùng dict

if room_type in rooms_available:
    if rooms_available[room_type] > 0:
        print(f"Phòng {room_type} có sẵn. Bạn có thể đặt phòng.")
    else:
        print(f"Phòng {room_type} hiện đã hết. Xin vui lòng chọn loại phòng khác.")
else:
    print("Loại phòng bạn yêu cầu không tồn tại.")


#kiểm tra tến đăng nhập có đúng không 
user = {"username": "admin", "password": "admin123", "role": "administrator"} # dùng dict 
username_input = 'admin'
pass_input = 'admin123'
if username_input == user["username"] and pass_input == user["password"]:
    print(f"dang nhap thanh cong, chao mung {user['role']}")
   
else:
    print("sai ten hoac mat khau")
