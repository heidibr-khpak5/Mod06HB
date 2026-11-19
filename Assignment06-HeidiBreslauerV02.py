# ------------------------------------------------------------------------------------------ #
# Title: Assignment06 Heidi's desperate plea
# Desc: This assignment demonstrates using class, exception handling
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   HBreslauer, 11/18/2026 2:42 pm get ready to do it.
#   HeidiBreslauer, 11/18/20 3:42pm. Created a shell of program including class,
#     def functions, included comment blocks and lots of pass.
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
#Define the Data Constants

FILE_NAME: str = "Enrollments.json"

#Define variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


"""
Description: for creation of new things
Change Log:
    HeidiBreslauer, 11/18/2026 Created function
    HeidiBreslauer, 11/18/20 3:42pm. Created a shell of program including class,
    def functions, included comment blocks and lots of pass.
    
"""
# class and functions definition
class FileProcessor:
    """
    File handling
    change log
        HBreslauer, 11/18/2026. Create the classes and functions I will need
        .
    """
    @staticmethod
    def read_data_from_file(file_name:str, student_data: list):
        file = None
        """
        Description: read data from json file and
            check for no file
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function
            HeidiBreslauer, 11/18/2026 added old function and modified it

        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
                IO.output_error_messages( "Please check that \
                 the file exists and that it is in a json \
                 format.")

        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()


    @staticmethod
    def write_data_to_file(file_name:str, student_data: list):
        file = None
        """
        Description: write list to json file
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function

        """
        try:
            file = open(file_name  , "w")
            json.dump(student_data, file)
        except TypeError as e:
            IO.output_error_messages("Please check that the data "
                                     "is a valid json file.")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()


class IO:
    """
    Description:
    Change Log:
        HeidiBreslauer, 11/18/2026 Created class

    """

    @staticmethod
    def output_error_messages(message: str, error: Exception=None):

        """
        Description: Handle error messages using Exceptions
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function
        return None
        """
        print(message, end="\n\n", sep="\n")
        if error is not None:
            print("--Technical Error Message --")
            print(error, error.__doc__, type(error),sep = "\n")



    @staticmethod
    def output_menu(menu:str):
        """
        Description: Prints out menu for user choices
        :return :None
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function

        """
        print()
        print("_"*50)
        print(menu)
        print("_"*50)





    @staticmethod
    def input_menu_choice():
        """
        Description: Get the users choice of functions
        :return: string with the users choice
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function

        """
        menu_choice = "0"
        try:
            menu_choice = input("Enter your menu choice number: ")
            if menu_choice not in ("1","2","3","4"):
                raise Exception as e:
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return menu_choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        Description: menu 1 register student
        :return: students
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function

        """
        pass
    @staticmethod
    def output_student_courses(student_data: list):
        """
        Description: print current students and their course
        :return: None
        Change Log:
            HeidiBreslauer, 11/18/2026 Created function

        """
        pass



# Beginning the main body of this script

# Read in data
    students =

# while running script
while True

    # present menu
    IO.output_menu(menu=MENU)

    # get menu choice and process
    menu_choice= IO.input_menu_choice()

    if menu_choice =="1": # Take input from user
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2": # print data
        IO.output_student_courses()
        continue

    elif menu_choice =="3": #write data to file
        FileProcessor.write_data_to_file(file_name: str, student_data: list)
        continue

    elif menu_choice =="4":
        print("Good Bye.")
        break



#old Stuff
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except Exception as e:
    print("Error: There was a problem with reading the file.")
    print("Please check that the file exists and that it is in a json format.")
    print("-- Technical Error Message -- ")
    print(e.__doc__)
    print(e.__str__())
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()


# Present and Process the data
while (True):

    # # Present the menu of choices
    # print(MENU)
    # menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
