import data
import menu
import helpers



while True:
    employees = data.load_data('employee_db.txt').readlines()
    option = int(menu.show_menu())
    if option == menu.SHOW_ALL_EMPLOYEES:
        menu.show_all(employees)
    elif option == menu.SHOW_EMPLOYEE:
        menu.show(employees)
    elif option == menu.CHANGE_SALARY:
        employees = menu.change_salary(employees)
        data.save_data('employee_db.txt', employees)
    elif option == menu.ADD_EMPLOYEE:
        employeeId, fName, lName, email, salary = menu.add_employee(employees)
        employees = data.add_employee(employees, employeeId, fName, lName, email, salary)
        data.save_data('employee_db.txt', employees)
    elif option == menu.DELETE_EMPLOYEE:
        employee_position, employee = menu.remove_employee(employees)
        employees = data.remove_employee(employees, employee_position, employee)
        data.save_data('employee_db.txt', employees)
    elif option == menu.GIVE_BONUS:
        bonus = menu.save_bonus_info(employees)

        bonus_db = data.save_bonus_info(employees, bonus)

        data.save_data('bonus_db.txt', bonus_db)
    elif option == menu.REPORT:        
        average, hSalary, hsEmployees = menu.cli_report(employees)

        data.file_report('report.txt', average, hSalary, hsEmployees)
    elif option == menu.QUIT:        
        menu.quit()
        break
# etc etc