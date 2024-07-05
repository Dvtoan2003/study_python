class Employee:
    co_salary = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)

    def __str__(self):
        return f'{self.fullname()} - {self.email} - Pay: {self.pay}'


class Developer(Employee):
    co_salary = 1.02

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang

    def __str__(self):
        return f'{super().__str__()} - Language: {self.pro_lang}'


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

    def __str__(self):
        return f'{super().__str__()} - Manages: {len(self.employees)} employees'


class Secretary(Employee):
    co_salary = 1.05

    def __init__(self, first, last, pay, job):
        super().__init__(first, last, pay)
        self.job = job

    def __str__(self):
        return f'{super().__str__()} - Job: {self.job}'


# Quản lý nhân viên
employees = {}


def add_employee(employee):
    if employee.email not in employees:
        employees[employee.email] = employee
        print(f"Added: {employee}")
    else:
        print(f"Employee with email {employee.email} already exists!")


def remove_employee(email):
    if email in employees:
        removed_emp = employees.pop(email)
        print(f"Removed: {removed_emp.fullname()}")
    else:
        print(f"No employee found with email {email}")


def show_all_employees():
    if employees:
        for emp in employees.values():
            print(emp)
    else:
        print("No employees to display.")


def find_employee(email):
    if email in employees:
        print(employees[email])
    else:
        print(f"No employee found with email {email}")


# Giao diện dòng lệnh
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Developer")
        print("2. Add Manager")
        print("3. Add Secretary")
        print("4. Remove Employee")
        print("5. Show All Employees")
        print("6. Find Employee by Email")
        print("7. Apply Salary Coefficient to All")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            pay = int(input("Pay: "))
            lang = input("Programming Language: ")
            dev = Developer(first, last, pay, lang)
            add_employee(dev)

        elif choice == '2':
            first = input("First Name: ")
            last = input("Last Name: ")
            pay = int(input("Pay: "))
            man = Manager(first, last, pay)
            add_employee(man)

        elif choice == '3':
            first = input("First Name: ")
            last = input("Last Name: ")
            pay = int(input("Pay: "))
            job = input("Job Description: ")
            sec = Secretary(first, last, pay, job)
            add_employee(sec)

        elif choice == '4':
            email = input("Enter employee email to remove: ")
            remove_employee(email)

        elif choice == '5':
            show_all_employees()

        elif choice == '6':
            email = input("Enter employee email to find: ")
            find_employee(email)

        elif choice == '7':
            for emp in employees.values():
                emp.apply_co_salary()
            print("Applied salary coefficient to all employees.")

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



