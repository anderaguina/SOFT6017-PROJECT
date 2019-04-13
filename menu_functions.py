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
    
def change_salary(employee_db, employee_id, salary):
    
    employee_position = helper_functions.find_employee(employee_db, employee_id)

    if employee_id == -1:
        return -1

    employee_to_modify = employee_db[employee_position]

    employee_attributes = employee_to_modify.split(',')

    employee_attributes[4] = salary

    employee_to_modify = employee_attributes[0] + ',' + employee_attributes[1] + ',' + \
        employee_attributes[2] + ',' + employee_attributes[3] + ',' + employee_attributes[4] + '\n'

    employee_db[employee_position] = employee_to_modify
    return employee_db

def add_employee(employee):
    print(f'Add employee')

def remove_employee(employee_db, employee_id):
    employee_position = helper_functions.find_employee(employee_db, employee_id)

    if employee_id == -1:
        return -1

    employee_db[employee_position] = ''
    return employee_db

def save_bonus_info():
    print('Save bonus info')

def generate_report():
    print('Generate report')