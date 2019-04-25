import menu_functions
import helper_functions


def load_data():
    employee_db = open("employee_db.txt","r")
    
    return employee_db


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


def save_data(employee_db):
    with open('employee_db.txt', 'w') as f:
        for employee in employee_db:
            attr = employee.split(',')
            if '\n' in employee:
                f.write(employee)
            else:
                f.write(employee + '\n')

def main():
    
    while True:

        employee_db = load_data().readlines()

        selected_option = show_menu()

        bonus_db = []

        # Switch -> case not available without dicts

        # Option 1
        if selected_option == '1':
            menu_functions.show_all_employees(employee_db)
            
        # Option 2
        elif selected_option == '2':
            employee_id = input('Employee id: ')
            menu_functions.show_employee(employee_db, employee_id)

        # Option 3
        elif selected_option == '3':
            print(f'------------------------CHANGE SALARY FOR EMPLOYEE-------------------------\n')

            employee_id = input('Employee id: ')
            print('\n')
            employee_position = helper_functions.find_employee(employee_db, employee_id)
            
            if employee_position == -1:
                print(f'### Employee with id {employee_id} not found ###')
            else:
                while True:
                    salary = input('New salary: ')
                    print('\n')

                    if int(salary) < 0:
                        print(f'Introduce a valid salary, bigger than 0')
                    else:
                        break

                employee_db = menu_functions.change_salary(employee_db, employee_id, salary)

                save_data(employee_db)

                print(f'$$$ Salary changed to {salary} $$$\n')
            
        # Option 4
        elif selected_option == '4':
            modified_employee_db = menu_functions.add_employee(employee_db)

            save_data(modified_employee_db)

        # Option 5              
        elif selected_option == '5':
            print(f'----------------------REMOVE EMPLOYEE-------------------------\n')

            employee_id = input('Employee id: ')
            print('\n')
            employee_position = helper_functions.find_employee(employee_db, employee_id)
            
            if employee_position == -1:
                print(f'### Employee with id {employee_id} not found ###')
            else:
                employee_db = menu_functions.remove_employee(employee_db, employee_id)

                save_data(employee_db)
                
                print(f'### Employee with id {employee_id} removed ###\n')

        # Option 6
        elif selected_option == '6':
            print(f'----------------------END OF YEAR BONUS AMOUNT-------------------------\n')

            bonus_amount = input('Bonus % amount: ')
            print('\n')

            bonus_db = menu_functions.save_bonus_info(employee_db, bonus_amount)

        # Option 7
        elif selected_option == '7':
            #print(f'----------------------GENERATE REPORT-------------------------\n')
            menu_functions.generate_report(employee_db)

        # Option 8
        elif selected_option == '8':
            print('GOODBYE!')
            break


if __name__ == '__main__':
    main()