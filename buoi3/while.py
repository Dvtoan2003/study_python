i = 0
while i < 7:
    print(i)
    i += 1

# sử dụng continue
number = 0
while number < 10:
    number += 1
    if number % 2 == 0: #nếu số đó chia hết cho 2 thì sẽ k lặp 
        continue
    print("Odd number:", number)


# vòng lặp while với list python
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print("Fruit:", fruits[index])
    index += 1

password = ""
while password != "12345":
    password = input("Enter the password: ")
    if password != "12345":
        print("Wrong password, try again.")
print("Access granted!")