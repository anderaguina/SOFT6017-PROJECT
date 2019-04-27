def load_data(filename):
    employee_db = open(filename, "r")
    
    return employee_db

def save_data(filename, employees):
    with open(filename, 'w') as f:
        for employee in employees:
            if '\n' in employee:
                f.write(employee)
            else:
                f.write(employee + '\n')


def file_report(filename, average, hSalary, hsEmployees):
    with open(filename, 'w') as f:
        f.write('----------PRINTED REPORT----------\n')
        f.write(f'Average salary = {average}\n')
        f.write(f'Highest salary = {float(hSalary)}\n')
        if len(hsEmployees) > 1:
            f.write(f'Highest salary employees are:\n')
        else:
            f.write(f'Highest salary employee is:\n')
        for employee in hsEmployees:
            f.write(f'-{employee}\n')


# Employee modification functions

def change_salary(employees, employee_position, salary):

    employee_to_modify = employees[employee_position]

    employee_attributes = employee_to_modify.split(',')

    employee_attributes[4] = salary

    employee_to_modify = employee_attributes[0] + ',' + employee_attributes[1] + ',' + \
        employee_attributes[2] + ',' + employee_attributes[3] + ',' + employee_attributes[4]

    employees[employee_position] = employee_to_modify

    return employees

def add_employee(employees, id, fName, lName, email, salary):

    new_employee = str(id) + ',' + fName + ',' + lName \
        + ',' + email + ',' + str(salary)

    employees.append(new_employee)

    return employees

def remove_employee(employees, employee_position, employee):

    print(f'### Removing employee with id {employee} ###\n')

    employees.pop(employee_position)

    return employees

def save_bonus_info(employees, bonus):
    bonus_db = []

    for employee in employees:
        attr = employee.split(',')
        
        employee_id = attr[0]
        employee_name = attr[1]
        employee_salary = attr[4]

        bonus_percentage = float(1) + float(int(bonus)/100)
        employee_bonus_value = float(employee_salary)*bonus_percentage

        employee_bonus_details = employee_id + ',' + employee_name + ',' + str(employee_bonus_value) + '\n'
        
        bonus_db.append(employee_bonus_details)

    return bonus_db
