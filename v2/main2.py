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
        employees = menu.change_salary(employees)
        data.save_data('test.txt', employees)
    elif option == menu.ADD_EMPLOYEE:
        employeeId, fName, lName, email, salary = menu.add_employee(employees)
        employees = data.add_employee(employees, employeeId, fName, lName, email, salary)
        data.save_data('test.txt', employees)
    elif option == menu.DELETE_EMPLOYEE:
        employee_position, employee = menu.remove_employee(employees)
        employees = data.remove_employee(employees, employee_position, employee)
        data.save_data('test.txt', employees)
    elif option == menu.GIVE_BONUS:
        bonus = menu.save_bonus_info(employees)

        bonus_db = data.save_bonus_info(employees, bonus)

        data.save_data('test2.txt', bonus_db)
    elif option == menu.REPORT:        
        average, hSalary, hsEmployees = menu.cli_report(employees)

        data.file_report('report2.txt', average, hSalary, hsEmployees)

# etc etc