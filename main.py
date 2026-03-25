# ---------------------------------------------------------
#                  Main Execution Script
# ---------------------------------------------------------

# Imports global state variables from shared_objects.py file.
import shared_objects

# Imports function module from functions.py file for menu display and data handling.
import functions

# ---------------------------------------------------------
#                    Main Program Loop:
# ---------------------------------------------------------

# Main loop for navigating menus based on user input.
while shared_objects.employee_db:

    # If statement that displays the main menu and allows the user to begin inputting navigational keystrokes.
    if shared_objects.main_menu:
        functions.main()
        menu_input = input('')

        # If user presses '1' key they are ported to the view employee menu where all employees and their data is displayed.
        if menu_input == '1':
            shared_objects.main_menu = False
            shared_objects.view_employees_menu = True

        # If the user presses '2' key they are ported to the add employee menu where they can input a new employees data into the system.
        elif menu_input == '2':
            shared_objects.main_menu = False
            shared_objects.add_employee_menu = True

        # If the user presses '3' key the employee data stored in employees.txt is imported into the program.
        elif menu_input == '3':
            functions.import_employee_data()
            print('Employee Data Import Complete')
            shared_objects.main_menu = True

        # If the user presses '4' key the employee data stored in the program is exported, updating employees.txt.
        elif menu_input == '4':
            functions.export_employee_data()
            print('Employee Data Export Complete')
            shared_objects.main_menu = True

        # If the user presses 'q' key they are ported out of the main menu and the program is terminated.
        elif menu_input == 'q':
            shared_objects.employee_db = False
            print(f'\n         Goodbye!')

        # If the user inputs anything else the program responds with 'Invalid Input'.
        else:
            print(f'         Invalid Input')

    # If statement that initializes the employee add menu, connected to the '2' keystroke.
    elif shared_objects.add_employee_menu:
        functions.add_employee()
        shared_objects.add_employee_menu = False
        shared_objects.main_menu = True

    # If statement that initializes the view employee menu, connected to the '1' keystroke.
    elif shared_objects.view_employees_menu:
        functions.view_employees()

        # If statement stating that if there are no employees stored then the terminal will inform the user and then 'continue' back to the main menu.
        if not shared_objects.employees:
            shared_objects.view_employees_menu = False
            shared_objects.main_menu = True
            continue

        menu_input = input('')

        # If statement that allows the user to remove an employee from the database by inputting their respective SSN once initialized with the 'd' keystroke.
        if menu_input == 'd':
            delete_employee_ssn = int(input(f'         Enter Employee SSN to Delete: '))
            found = False

            for emp_id, emp_data in shared_objects.employees.items():

                # Checks to see if the respective employee SSN exists in the system before executing delete. Then informs the user the deletion was successful.
                if emp_data[1] == delete_employee_ssn:
                    del shared_objects.employees[emp_id]
                    shared_objects.employee_counter -= 1
                    print(f'\n         Employee deleted successfully. ')
                    found = True
                    break

            # If the SSN is not found inform the user.
            if not found:
                print(f'\n         Employee not found. ')

        # If statement that allows the user to return to the main menu with the 'm' keystroke.
        elif menu_input == 'm':
            shared_objects.view_employees_menu = False
            shared_objects.main_menu = True

        # If statement that allows the user to search for a specific user to display by inputting their respective SSN. Done by pressing the 's' key.
        elif menu_input == 's':
            if functions.search_ssn():
                shared_objects.view_employees_menu = False
                shared_objects.employee_data_menu = True

            # Else statement closing the conditional saying if else besides what has been specified print 'Employee not found'.
            else:
                print(f'\n         Employee not found. ')
        else:
            print('\n         Invalid input. ')

    # If statement that initializes the employees personal data menu.
    elif shared_objects.employee_data_menu:
        functions.employee_data(shared_objects.selected_employee_id)
        menu_input = input('')

        # If statement that allows the user to return to the previous menu with the 'b' keystroke.
        if menu_input == 'b':
            shared_objects.employee_data_menu = False
            shared_objects.view_employees_menu = True

        # If statement that allows te user to return to the main menu with the 'm' keystroke.
        elif menu_input == 'm':
            shared_objects.employee_data_menu = False
            shared_objects.main_menu = True

        # If statement that allows the user to activate the edit employee function with the 'e' keystroke.
        elif menu_input == 'e':
            functions.edit_employee()

        # If the user inputs anything else the program responds with 'Invalid Input'.
        else:
            print('\n         Invalid input. ')