def load_data(filename):
    employee_db = open(filename, "r")
    
    return employee_db

def save_employees(filename, employees):
    with open(filename, 'w') as f:
        for employee in employees:
            if '\n' in employee:
                f.write(employee)
            else:
                f.write(employee + '\n')


def report(filename, employees):
    pass


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

