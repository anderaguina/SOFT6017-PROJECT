import helper_functions

# Menu functions
def show_all_employees(employee_db):

    print(f'------------------------LIST OF EMPLOYEES-------------------------\n')

    for employee in employee_db:
        print(employee)
    
    # print(f'\n-----------------------------------------------------------------\n')
    
def show_employee(employee_db, employee_id):

    employee_position = helper_functions.find_employee(employee_db, employee_id)
    
    print(f'------------------------SEARCH FOR EMPLOYEE-------------------------\n')

    if employee_position == -1:
        print(f'Employee with id {employee_id} not found')
    else:
        print(f'Employee found\n')
        print(employee_db[employee_position])
    
def change_salary(salary):
    print(f'Change salary {salary}')

def add_employee(employee):
    print(f'Add employee')

def remove_employee(employee):
    print(f'Remove employee')

def save_bonus_info():
    print('Save bonus info')

def generate_report():
    print('Generate report')