import menu_functions

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


def save_data():
    print('Save data')

def main():
    employee_db = load_data().readlines()
    
    while True:
        selected_option = show_menu()

        # Switch -> case not available without dicts
        if selected_option == '1':
            menu_functions.show_all_employees(employee_db)
        elif selected_option == '2':
            employee_id = input('Employee id: ')
            menu_functions.show_employee(employee_db, employee_id)
        elif selected_option == '3':
            pass
        elif selected_option == '4':
            pass
        elif selected_option == '5':
            pass
        elif selected_option == '6':
            pass
        elif selected_option == '7':
            pass
        elif selected_option == '8':
            break

    # save_data()


if __name__ == '__main__':
    main()