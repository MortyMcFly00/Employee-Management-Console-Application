# ---------------------------------------------------------
#                 Shared Global Module
# ---------------------------------------------------------

# Dictionary that stores employee records using unique numeric IDs as keys.
employees = {}

# Starting value for automatically assigned employee IDs.
employee_id: int = 1000

# Counter that tracks how many employees have been added during this session.
employee_counter = 0

# Tracks the ID of the employee currently being viewed or edited.
selected_employee_id = None

# Menu state flags used to control program flow between different interfaces.
employee_db = True             # Main loop control flag (True while program runs)
main_menu = True               # Flag to display the main menu
view_employees_menu = False    # Flag to display the view employees screen
add_employee_menu = False      # Flag to display the add employee screen
employee_data_menu = False     # Flag to display the individual employee screen
