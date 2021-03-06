import random
import json
import string


# Helper functions
def find_employee(employee_db, employee_id):
    employee_position = 0
    for employee in employee_db:
        employee_attributes = employee.split(',')

        if(employee_attributes[0] != employee_id):
            employee_position+=1
        else:
            break
        if employee_position >= len(employee_db):
            return -1

    return employee_position

def generate_unique_id(employee_db):
    employee_ids = read_employee_ids(employee_db)
    while True:
        unique_id = random.randint(0, 99999)
        if str(unique_id) not in employee_ids:
            return unique_id

def generate_unique_email(name, last_name, employee_db):

    employee_emails = read_employee_emails(employee_db)
    while True:
        name_extra = ''.join(random.choice(string.digits))
    
        email = name.lower() + '.' + last_name.lower() + name_extra + '@mycit.ie'
        
        if email not in employee_emails:
            return email
    

    return email

def read_employee_ids(employee_db):
    employee_ids = []
    for employee in employee_db:
        employee_attributes = employee.split(',')
        employee_ids.append(employee_attributes[0])
    
    return employee_ids

def read_employee_emails(employee_db):
    employee_emails = []
    for employee in employee_db:
        employee_attributes = employee.split(',')
        employee_emails.append(employee_attributes[3])
    
    return employee_emails

def calculate_average_salary(employee_db):
    salaries = 0
    number_of_employees = len(employee_db)

    for employee in employee_db:
        attr = employee.split(',')
        if '\n' in attr[4]:
            attr[4] = attr[4][:-2]
        salaries = salaries + float(attr[4])

    average = salaries / number_of_employees

    return average

def highest_salary(employee_db):

    highest_salary = 0

    highest_salary_employees = []

    for employee in employee_db:
        attr = employee.split(',')
        
        employee_salary = attr[4]

        print('Employee_salary = ', float(employee_salary))
        print('Highest_salary = ', float(highest_salary))
        print('len = ', len(highest_salary_employees))

        if float(employee_salary) > float(highest_salary):
            highest_salary = employee_salary
            
            for x in range(len(highest_salary_employees)):
                print('pop')
                print('x = ', x)
                print('len = ', len(highest_salary_employees))
                print(f'poped employee in {len(highest_salary_employees) - 1}')
                highest_salary_employees.pop(len(highest_salary_employees) - 1)

            highest_salary_employees.append(attr[1])
        elif float(employee_salary) == float(highest_salary):
            highest_salary_employees.append(attr[1])
    return highest_salary, highest_salary_employees

def write_report_to_file(average, highest_salary, highest_salary_employees):
    with open('report.txt', 'w') as f:
        f.write('----------PRINTED REPORT----------\n')
        f.write(f'Average salary = {average}\n')
        f.write(f'Highest salary = {float(highest_salary)}\n')
        if len(highest_salary_employees) > 1:
            f.write(f'Highest salary employees are:\n')
        else:
            f.write(f'Highest salary employee is:\n')
        for employee in highest_salary_employees:
            f.write(f'-{employee}\n')
