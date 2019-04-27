import data
import menu
import helpers

# use argparse to get arguments such as employee db filename, report filename, debug flag etc - use some default values for each, ie employees.txt for employee db name etc

while True:
    employees = data.load_data('test.txt').readlines()
    option = menu.show_menu()
    if int(option) == menu.SHOW_ALL_EMPLOYEES:
        menu.show_all(employees)
    elif int(option) == menu.SHOW_EMPLOYEE:
        employeeId = input("employee id: ")
        menu.show(employees, employeeId)
    elif int(option) == menu.CHANGE_SALARY:
        employeeId = input("employee id: ")
        employees = menu.change_salary(employees, employeeId)
        data.save_employees('test.txt', employees)
# etc etc