# ---------------------------------------------------------
#               Employee Database Functions
# ---------------------------------------------------------

# Imports global state variables from shared_objects.py file.
import shared_objects

# ---------------------------------------------------------
#                  Menu Display Function
# ---------------------------------------------------------

# Function displaying the main menu UI, navigation options, and the current employee count.
def main():
    print(f'------------------------------------Employee Database Log-------------------------------------\n')
    print(f' \n')
    print(f'         Directory Navigation: \n')
    print(f'                                   1: View Employees \n')
    print(f'                                   2: Add Employee \n')
    print(f'                                   3: Import Employee Data \n')
    print(f'                                   4: Export Employee Data \n')
    print(f' \n')
    print(f'                 There are ({len(shared_objects.employees)}) employees in the system. \n')
    print(f' \n')
    print(f'    Press 1 to View | Press 2 to Add | Press 3 to Import | Press 4 to Export | Press q to quit\n')

# ---------------------------------------------------------
#                  Add / Edit Functionality
# ---------------------------------------------------------

# Function that displays the menu where the user can add a new employee and store their data in an employee ID container.
def add_employee():

    # Collects employee data for all required fields.
    print(f'-------------------------------Add Employee Data-------------------------------\n')
    print(f' \n')
    employee_name = input(f'         Enter Employee Name: ')
    employee_ssn = input(f'         Enter Employee SSN: ')
    employee_phone = input(f'         Enter Employee Phone: ')
    employee_email = input(f'         Enter Employee Email: ')
    employee_salary = float(input(f'         Enter Employee Salary: '))
    print(f' \n')
    print(f'                           Press m to return to main menu\n')

    # Store employee data under the current employee_id key
    shared_objects.employees[shared_objects.employee_id] = [employee_name, employee_ssn, employee_phone, employee_email, employee_salary]

    print(f'\n         Employee {employee_name} added with ID {shared_objects.employee_id}.\n')
    # Increment both ID and employee count
    shared_objects.employee_id += 1
    shared_objects.employee_counter += 1

# Function that allows user to update the fields of a selected employee one by one.
def edit_employee():

    # Pulls the specified employees data in shared_objects.py to be edited by using the global variable selected ID.
    employee = shared_objects.employees[shared_objects.selected_employee_id]

    # Shows current name and asks the user to input a new on if applicable. 'Press Enter to Keep existing".
    print(f'Current name: {employee[0]}')
    new_name = input('Enter new name (Press Enter to keep current): ')
    if new_name.strip():    # strip() function for input sanitization.
        employee[0] = new_name    # assigns the string value placed in new_name and copies it to element [0] in employees.

    # Shows current SSN and asks the user to input a new on if applicable. 'Press Enter to Keep existing".
    print(f'Current SSN: {employee[1]}')
    new_ssn = input('Enter new SSN (Press Enter to keep current): ')
    if new_ssn.strip():    # strip() function for input sanitization.
        employee[1] = new_ssn    # assigns the string value placed in new_ssn and copies it to element [1] in employees.

    # Shows current phone number and asks the user to input a new on if applicable. 'Press Enter to Keep existing".
    print(f'Current phone number: {employee[2]}')
    new_phone = input('Enter new phone number (Press Enter to keep current): ')
    if new_phone.strip():    # strip() function for input sanitization.
        employee[2] = new_phone    # assigns the string value placed in new_phone and copies it to element [2] in employees.

    # Shows current email address and asks the user to input a new on if applicable. 'Press Enter to Keep existing".
    print(f'Current email address: {employee[3]}')
    new_email = input('Enter new email address (Press Enter to keep current): ')
    if new_email.strip():    # strip() function for input sanitization.
        employee[3] = new_email    # assigns the string value placed in new_email and copies it to element [3] in employees.

    # Shows current salary and asks the user to input a new on if applicable. 'Press Enter to Keep existing".
    print(f'Current salary: {employee[4]}')
    new_salary = input('Enter new salary (Press Enter to keep current): ')
    if new_salary.strip():    # strip() function for input sanitization.
        employee[4] = float(new_salary)    # assigns the string value placed in new_salary and copies it to element [4] in employees and converts it to a float.

# ---------------------------------------------------------
#                   View/Search Functionality
# ---------------------------------------------------------

# Function that displays the contents of the dictionary, listing out all employees in the system.
def view_employees():
    print(f'-------------------------------Employee List-------------------------------\n')

    # If no employees are stored, inform the user.
    if not shared_objects.employees:
        print(f'         No employees have been added yet. \n')

    # Otherwise, print each employee's fully formatted list of data, organized by who was placed in the dictionary first.
    else:
        for emp_id in shared_objects.employees:
            emp = shared_objects.employees[emp_id]
            print(f'------------------------------- {emp[0]} -------------------------------\n')
            print(f'         SSN: {emp[1][:3]}-{emp[1][3:5]}-{emp[1][5:]}\n')
            print(f'         Phone: ({emp[2][:3]}) {emp[2][3:6]}-{emp[2][6:]}\n')
            print(f'         Email: {emp[3]}\n')
            print(f'         Salary: ${float(emp[4]):,.2f}\n')
            print('--------------------------------------------------------------------------------\n')

    print(f'      Press s to Search by SSN | Press m to return to main menu\n')

# Function that enables the user to pull a single employees data by inputting their full SSN.
def search_ssn():

    employee_ssn = input('Enter SSN: ')

    # Renames the key and value signature from the employees dictionary to emp_id and emp_data respectively.
    # Uses the .items() function to access both the ID and full employee record in one loop.
    for emp_id, emp_data in shared_objects.employees.items():

        # If statement saying that if the second element (SSN) in the employee's data matches the input,
        # store that employee’s ID and return True to confirm match.
        if emp_data[1] == employee_ssn:
            shared_objects.selected_employee_id = emp_id
            return True

    # Otherwise inform the user that the employee was not located.
    print('Employee not found.')
    return False


# Function that displays the details of the specified employee.
def employee_data(selected_id):

    if selected_id in shared_objects.employees:
        emp = shared_objects.employees[selected_id]
        print(f'-------------------------------{emp[0]}-------------------------------\n')
        print(f' \n')

        # Checks if the specified employee ID is present in the system.
        print(f'         Name: {emp[0]} \n')

        # String slicing to format SSN, phone number, and salary for improved readability.
        print(f'         SSN: {emp[1][:3]}-{emp[1][3:5]}-{emp[1][5:]} \n')
        print(f'         Phone: ({emp[2][:3]}) {emp[2][3:6]}-{emp[2][6:]} \n')
        print(f'         Email: {emp[3]} \n')
        print(f'         Salary: ${float(emp[4]):,.2f}\n')

    # Prints employee not found if the specified employee is not stored in the system.
    else:
        print(f'         Employee not found. \n')

    print(f' \n')
    print(f'                Press b to Go Back | Press e to Edit | Press m to Return to Main Menu\n')

# ---------------------------------------------------------
#           Import \ Export Functionalities
# ---------------------------------------------------------

# Appends new employees to employees.txt (avoids duplicate IDs)
def export_employee_data():
    # Creates an empty set to store existing employee IDs that are already written in the file.
    # This prevents the program from duplicating entries when exporting multiple times in a session.
    existing_ids = set()

    try:
        # Tries to open the employees.txt file in read mode to gather all previously saved employee IDs.
        with open('employees.txt', 'r') as file:
            for line in file:
                # Removes any newline characters and whitespace, then splits each line by commas.
                parts = line.strip().split(',')

                # Takes the first element (employee ID), converts it to an integer, and adds it to the existing_ids set.
                existing_ids.add(int(parts[0]))

    # If the file does not exist, the program skips this step without error and proceeds to create it in write mode.
    except FileNotFoundError:
        pass


    # Opens the employees.txt file in append mode. This allows the program to write new employees
    # without erasing or modifying any previously saved data in the file.
    with open('employees.txt', 'a') as file:

        # Loops through every employee currently stored in the program's in-memory dictionary.
        for emp_id, data in shared_objects.employees.items():

            # If the current employee ID is not already in the set of existing IDs,
            # that means this employee has not yet been exported and should be written to the file.
            if emp_id not in existing_ids:

                # Concatenates all elements of the employee data into a comma-separated line.
                # The line includes ID, name, SSN, phone, email, and salary, followed by a newline character.
                line = f"{emp_id},{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n"

                # Writes the formatted line to the text file.
                file.write(line)

    # Prints confirmation to the terminal letting the user know the export operation was completed.
    print('\nEmployees exported to employees.txt\n')


# Function that imports employee data from employees.txt back into the program's dictionary.
# This function is useful for restoring data that was previously saved to disk, allowing continuity across sessions.
def import_employee_data():

    # Resets the employees dictionary to ensure no old data remains before importing new records.
    shared_objects.employees = {}

    # Variable used to track the highest employee ID found in the file so the next new employee ID is not duplicated.
    highest_id = 1000

    try:
        # Attempts to open the employees.txt file in read mode.
        with open('employees.txt', 'r') as file:

            # Reads the file line-by-line, where each line represents a single employee record.
            for line in file:
                # Removes newlines and spaces, then splits the line into parts using commas.
                parts = line.strip().split(',')

                # The first element is the employee ID, used as the dictionary key.
                emp_id = int(parts[0])

                # The remaining elements are employee data. The salary (parts[5]) is converted back to a float.
                shared_objects.employees[emp_id] = parts[1:5] + [float(parts[5])]

                # If the imported employee ID is higher than the current highest_id,
                # update the highest_id value to ensure no new employees are assigned duplicate IDs.
                if emp_id > highest_id:
                    highest_id = emp_id

        # Updates the global employee_id counter to be one greater than the highest ID found during import.
        # This ensures the next added employee receives a new, unique ID.
        shared_objects.employee_id = highest_id + 1

    # If the file does not exist, the program informs the user and proceeds with an empty employee list.
    except FileNotFoundError:
        print('\nemployees.txt not found. Starting with empty list.\n')