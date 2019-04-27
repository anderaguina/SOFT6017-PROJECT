import data
import menu
import helpers

# use argparse to get arguments such as employee db filename, report filename, debug flag etc - use some default values for each, ie employees.txt for employee db name etc

while True:
    employees = data.load_data('test.txt').readlines()
    option = int(menu.show_menu())
    if option == menu.SHOW_ALL_EMPLOYEES:
        menu.show_all(employees)
    elif option == menu.SHOW_EMPLOYEE:
        menu.show(employees)
    elif option == menu.CHANGE_SALARY:
        employeeId = input("employee id: ")
        employees = menu.change_salary(employees, employeeId)
        data.save_employees('test.txt', employees)
    elif option == menu.ADD_EMPLOYEE:
        employeeId, fName, lName, email, salary = menu.add_employee(employees)
        employees = data.add_employee(employees, employeeId, fName, lName, email, salary)
        data.save_employees('test.txt', employees)
    elif option == menu.DELETE_EMPLOYEE:
        employeeId, fName, lName, email, salary = menu.add_employee(employees)
        employees = data.add_employee(employees, employeeId, fName, lName, email, salary)
        data.save_employees('test.txt', employees)
# etc etc