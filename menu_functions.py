import helper_functions


# Menu functions
def show_all_employees(employee_db):

    print(f'------------------------LIST OF EMPLOYEES-------------------------\n')

    for employee in employee_db:
        print(employee)
    
    # print(f'\n-----------------------------------------------------------------\n')
    
def show_employee(employee):
    print(f'Show specific employee {employee}')

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