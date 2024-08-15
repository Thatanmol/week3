# Initialize a global counter Registration IDs
registration_counter = 50000

def student_registration():
    global registration_counter # use the global counter

    # Generate the Registration ID using the current counter value
    registration_id = registration_counter
    registration_counter += 1 # Increment the counter for the next registration

    # collecting information from the user
    date = input("Enter the registration date(dd/mm/yyyy): ")
    student_id = input("Enter the student ID:")
    student_name = input("Enter the student Name: ")
    course_name = input("Enter the Course Name: ")

# Return the collected information and Registration ID
return date, student_id, student_name, course_name, registration_id

# call the function and get the data:
date, student_id, student_name, course_name, registration_id = student_registration()

# Print the information outside the function
print("\nPrinting Student Registration Information:")
print(f"Date: {date}")
print(f"Student ID: {student_id}")
print(f"student Name: {student_name}")
print(f"Course Name: {course_name}")
print(f"Registration ID: {registration_id}")