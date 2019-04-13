import menu_functions

def load_data():
    print('Load data')

def show_menu():
    print('1. View all employees')
    print('2. View a particular employee')
    print('3. Edit the salary of an employee')
    print('4. Add a new employee')
    print('5. Delete an employee')
    print('6. Give a bonus to each employee, writing the details to a file')
    print('7. Generate a report for management')
    print('8. Quit')
    option = input()
    return option


def save_data():
    print('Save data')

def main():
    # load_data()
    
    while True:
        selected_option = show_menu()

        if selected_option == '8':
            break

    # save_data()


if __name__ == '__main__':
    main()