class Employee:
    co_salary = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)


class Developer(Employee):
    co_salary = 1.02

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    co_salary = 1.5

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('--', emp.fullname())


class Secretary(Employee):
    co_salary = 1.05

    def __init__(self, first, last, pay, job):
        super().__init__(first, last, pay)
        self.job = job


# Tạo các đối tượng
dev1 = Developer("toan", "tai", 400, 'python')
dev2 = Developer("hien", "cho", 400, 'js')
sec1 = Secretary("ngoc", "trinh", 600, "eat with manager")

# Tạo đối tượng Manager
man1 = Manager('trump', 'dollar', 1000, [dev1, dev2])

# Sử dụng các phương thức của Manager
man1.remove_employee(dev1)  # Xóa dev1 khỏi danh sách
man1.add_employee(dev1)     # Thêm lại dev1 vào danh sách
man1.print_emp()            # In danh sách các nhân viên dưới quyền quản lý
