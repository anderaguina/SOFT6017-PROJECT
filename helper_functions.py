


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

def generate_unique_id():
    print('Generate unique id')

def generate_unique_email():
    print('Generate unique email')