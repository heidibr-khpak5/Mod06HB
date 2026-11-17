# ------------------------------------------------- #
# Title: Lab01 - Working with Functions
# Description: Demonstrates how to use functions in your code
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# HeidiBreslauer, 11/17/2026. Will do the Lab
# HeidiBreslauer, 11/17,2026. Final pass on mod06lab1
# ------------------------------------------------- #
import json

# Define the Data Constants
FILE_NAME: str = 'MyLabData.json'

# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ''  # Holds a custom message string.
menu_choice: str = ''   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data.
students: list = []  # a table of student data.
file_data: str = ''  # Holds json data.
file = None # This is the actual type of the file handler.

# define a function to read data
# When the program starts, read the file data into table
# Extract the data from the file
# Read from the JSON file
def read_data_from_file():
    global FILE_NAME
    global students
    global file
    try:
        file = open(FILE_NAME, "r")
        students = json.load(file)
    except FileNotFoundError as e:
        print("Text file must exist before running this script!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file is not None and file.closed == False:
            file.close()


def output_menu():
    global MENU
    global menu_choice

    print(MENU)
    menu_choice = input("Enter your choice number: ")
    print() #adding extra space to make it nice1



def output_letter_by_gpa():
    global message
    global students

    # Process the data to create and display a custom message

    print("-" * 50)
    for student in students:
        if float(student["GPA"]) >= 4.0:
            message = " {} {} earned an A with a {:.2f} GPA"
        elif float(student["GPA"]) >= 3.0:
            message = " {} {} earned a B with a {:.2f} GPA"
        elif float(student["GPA"]) >= 2.0:
            message = " {} {} earned a C with a {:.2f} GPA"
        elif float(student["GPA"]) >= 1.0:
            message = " {} {} earned a D with a {:.2f} GPA"
        else:
            message = " {} {}'s {:.2f} GPA was not a passing grade"

        print(message.format(student["FirstName"], student["LastName"],
                             float(student["GPA"])))
    print("-" * 50)


def input_student_data():
    global student_first_name
    global student_last_name
    global student_gpa
    global student
    global students

    try:
        # Input the data
        student_first_name = input("What is the student's first name? ")
        if not student_first_name.isalpha():
            raise ValueError("The first name should not contain numbers.")

        student_last_name = input("What is the student's last name? ")
        if not student_last_name.isalpha():
            raise ValueError("The last name should not contain numbers.")

        try:  # using a nested try block to capture when an input cannot be changed to a float
            student_gpa = float(input("What is the student's GPA? "))
        except ValueError:
            raise ValueError("GPA must be a numeric value.")

        student = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "GPA": float(student_gpa)}
        students.append(student)
    except ValueError as e:
        print(e)  # Prints the custom message
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')




def write_data_to_file():
    global file
    global students

    try:
        file = open(FILE_NAME, "w")
        json.dump(students, file)
    except TypeError as e:
        print("Please check that the data is a valid JSON format\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print("-- Technical Error Message -- ")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if file is not None and file.closed == False:
            file.close()

 # End of function definition

#Beginning of Main body of this script
#Get the data from the file
read_data_from_file()

# Repeat the following tasksile True:
while True:
    output_menu()

    if menu_choice == "1":
        output_letter_by_gpa()
        continue

    elif menu_choice == "2":
        input_student_data()
        continue

    elif menu_choice == "3":
        write_data_to_file()
        continue

    elif menu_choice == "4":
        print("Good Bye.")
        break  # out of the while loop








