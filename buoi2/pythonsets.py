#python Sets
# dùng len() để kiểm tra độ dài
#dùng add() để thêm phần tử, dùng remove() hoặc discard() để xoá phần tử, dùng clearn() để xoá hết set 
my_family = {'toan','vinh','chieu'}
my_family.add('hien')
print(my_family)

my_family_after = {'toan','vinh','chieu'}
my_family_before = {'hien'}
my_family_after.update(my_family_before)  #dùng update() để thêm set nọ vào set kia 
print(my_family_after)


# vòng lặpfor cho set python
set_number = {1,2,3,4,5,6}
total_sum = 0
for number in set_number: # vòng lặp for
    total_sum += number # tính tổng
print(f"Total Sum : {total_sum}")