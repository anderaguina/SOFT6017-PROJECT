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
        employee_attributes[2] + ',' + employee_attributes[3] + ',' + employee_attributes[4]

    employee_db[employee_position] = employee_to_modify
    return employee_db

def add_employee(employee_db):
    employee = []

    name = input('New employee name: ')
    last_name = input('New employee last name: ')
    
    while True:
        salary = input('New employee salary: ')
        if int(salary) >= 0:
            break
        else:
            print('Specify a valid salary, 0 for interns or > 0 for employees')
    
    unique_id = helper_functions.generate_unique_id(employee_db)
    email = helper_functions.generate_unique_email(name, last_name, employee_db)
    
    print(type(name))
    print(type(last_name))
    print(type(unique_id))
    print(type(email))
    print(type(salary))

    new_employee = str(unique_id) + ',' + name + ',' + last_name \
        + ',' + email + ',' + str(salary)

    employee_db.append(new_employee)

    return employee_db

def remove_employee(employee_db, employee_id):
    employee_position = helper_functions.find_employee(employee_db, employee_id)

    if employee_id == -1:
        return -1

    employee_db.pop(employee_position)

    return employee_db

def save_bonus_info(employee_db, bonus):

    bonus_db = []

    for employee in employee_db:
        attr = employee.split(',')
        
        employee_id = attr[0]
        employee_name = attr[1]
        employee_salary = attr[4]

        bonus_percentage = float(1) + float(int(bonus)/100)
        employee_bonus_value = float(employee_salary)*bonus_percentage

        employee_bonus_details = employee_id + ',' + employee_name + ',' + str(employee_bonus_value) + '\n'
        
        bonus_db.append(employee_bonus_details)

    with open('employee_bonus_db.txt', 'w') as f:
        f.write('Id, Name, Bonus\n')
        for employee in bonus_db:
            f.write(employee)

    return bonus_db

def generate_report(employee_db):
    average = helper_functions.calculate_average_salary(employee_db)

    highest_salary, highest_salary_employees = helper_functions.highest_salary(employee_db)

    print('------------- REPORT --------------')
    print(f'|Average salary: {average}|')
    print(f'|Highest salary:           {highest_salary}|')
    print(f'|Highest salary employees:        |')
    for employee in highest_salary_employees:
        print(f' -{employee}')
    print('-----------------------------------')

    helper_functions.write_report_to_file(average, highest_salary, highest_salary_employees)