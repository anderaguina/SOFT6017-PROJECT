import helpers
import data

SHOW_ALL_EMPLOYEES = 1
SHOW_EMPLOYEE = 2
CHANGE_SALARY = 3
ADD_EMPLOYEE = 4
DELETE_EMPLOYEE = 5
GIVE_BONUS = 6
REPORT = 7
QUIT = 8


def main():
    pass


def show_menu():
    print(f'\n------------------------------MENU-------------------------------\n')
    print('1. View all employees')
    print('2. View a particular employee')
    print('3. Edit the salary of an employee')
    print('4. Add a new employee')
    print('5. Delete an employee')
    print('6. Give a bonus to each employee, writing the details to a file')
    print('7. Generate a report for management')
    print('8. Quit')
    print(f'\n-----------------------------------------------------------------\n')
    option = input('Select an option from the menu: ')
    
    return option

def show_all(employees):
    print(f'------------------------LIST OF EMPLOYEES-------------------------\n')

    for employee in employees:
        print(employee)

def show(employees):
    
    print(f'------------------------SEARCH FOR EMPLOYEE-------------------------\n')
    employee = input("employee id: ")
    employee_position = helpers.find_employee(employees, employee)
    exists = helpers.employee_exists(employee_position, employee)
    if exists == 0:
        print(f'\nEmployee found:\n')
        print(employees[employee_position])

def change_salary(employees):
    print(f'------------------------CHANGE EMPLOYEE SALARY-------------------------\n')
    employee = input("employee id: ")
    while True:
        employee_position = helpers.find_employee(employees, employee)
        exists = helpers.employee_exists(employee_position, employee)

        if exists != 0:
            employee = input("employee id: ")
            employee_position = helpers.find_employee(employees, employee)
            exists = helpers.employee_exists(employee_position, employee)
        else:
            break
    
    while True:
        salary = input('New salary: ')
        if int(salary) < 0:
            print(f'Introduce a valid salary, bigger than 0')
        else:
            break
    
    employees = data.change_salary(employees, employee_position, salary)

    return employees

def add_employee(employees):
    print(f'------------------------ADD NEW EMPLOYEE-------------------------\n')
    fName = input('New employee name: ')
    lName = input('New employee last name: ')

    while True:
        salary = input('New employee salary: ')
        if int(salary) >= 0:
            break
        else:
            print('Specify a valid salary, 0 for interns or > 0 for employees')

    unique_id = helpers.generate_unique_id(employees)
    email = helpers.generate_unique_email(fName, lName, employees)

    return unique_id, fName, lName, email, salary
