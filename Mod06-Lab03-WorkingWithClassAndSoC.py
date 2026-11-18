# ------------------------------------------------- #
# Title: Lab03 Working with Class and SoC
# Description: Demonstrates how to use Class
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# HeidiBreslauer, 11/17/2026
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
student: dict = {}  # one row of student data.
students: list = []  # a table of student data.
file_data: str = ''  # Holds json data.
# file = None  # This is the actual type of the file handler.


# SoC Processing of functions working with json files
class FileProcessor
    """"
    ChangeLog: 
        HeidiBreslauer, 11/18/2026, created added def read from file
    """

    # When the function starts, read the file data into table
    # Extract the data from the file
    # Read from the JSON file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        # global FILE_NAME
        # global students
        # global file
        file = None

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!",e)
            #print("Text file must exist before running this script!\n")
            #print("-- Technical Error Message -- ")
            #print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            IO.output_error_messages(("There was a non-specific error!",e)
            #print("There was a non-specific error!\n")
            #print("-- Technical Error Message -- ")
            #rint(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()
        return student_data



class IO:
    """
    do IO work
    need at least one function in class. Why not in class FireProcessor?
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """this function displays a custom error message to userr
        ChangeLog: (who, when, what)
        HeidiBreslauer, 11/18/2026 added this new class

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")










def output_menu(menu: str):
    # global MENU
    # global menu_choice
    print()  # Adding extra space to make it look nicer.
    print(menu)
    menu_choice = input("Enter your menu choice number: ")  # note this for the next lab
    print()  # Adding extra space to make it look nicer.
    return menu_choice


def output_letter_by_gpa(student_data: list):
    # global message
    # global students

    # Process the data to create and display a custom message
    print("-" * 50)
    for student in student_data:
        if student["GPA"] >= 4.0:
            message = " {} {} earned an A with a {:.2f} GPA"
        elif student["GPA"] >= 3.0:
            message = " {} {} earned a B with a {:.2f} GPA"
        elif student["GPA"] >= 2.0:
            message = " {} {} earned a C with a {:.2f} GPA"
        elif student["GPA"] >= 1.0:
            message = " {} {} earned a D with a {:.2f} GPA"
        else:
            message = " {} {}'s {:.2f} GPA was not a passing grade"

        print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
    print("-" * 50)


def input_student_data(student_data: list):
    # global student_first_name
    # global student_last_name
    # global student_gpa
    # global student_row
    # global students

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
        student_data.append(student)
    except ValueError as e:
        print(e)  # Prints the custom message
        print("-- Technical Error Message -- ")
        print(e.__doc__)
        print(e.__str__())
    except Exception as e:
        print("There was a non-specific error!\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
    return student_data


def write_data_to_file(file_name: str, student_data: list):
    # global file
    # global students
    file = None

    try:
        file = open(file_name, "w")
        json.dump(student_data, file)
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


#  End of function definitions


# Beginning of the main body of this script
students = read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the following tasks
while True:

    menu_choice = output_menu(menu=MENU)

    if menu_choice == "1":
        output_letter_by_gpa(student_data=students)
        continue

    elif menu_choice == "2":
        students = input_student_data(student_data=students)
        continue

    elif menu_choice == "3":
        write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break  # out of the while loop
