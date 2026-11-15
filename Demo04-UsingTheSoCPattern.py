# ------------------------------------------------- #
# Title: Demo04 - Separation of Concerns
# Description: Demonstrates how to use classes and function with the Separation of Concerns pattern
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script

# Notes: You will learn about complex data classes in module 07

# ------------------------------------------------- #

class Results:  # Data Layer
    """
    A collection of variables to hold arithmetic results Data

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """
    sum: float = 0.0
    difference: float = 0.0


class Calculator:  # Processing Layer
    """
    A collection of functions that perform arithmetic Processing

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def add(a: float, b: float):
        """ This function adds to values and returns a sum

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param a: float data used as the first number
        :param b: float data used as the second number
        :return: float data with the sum of the first and second numbers
        """

        return a + b

    @staticmethod
    def subtract(a: float, b: float):
        """ This function adds to values and returns a sum

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param a: float data used as the first number
        :param b: float data used as the second number
        :return: float data with the difference between the first and second numbers
        """

        return a - b


class IO:  # Presentation Layer
    """
    A collection of functions that present or gather user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def display_results(results: list, display_format: str):
        """ This function displays result values in a given format

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param results: The list of results you want to display
        :param display_format: The display format (message, csv, or json)
        :return: None
        """
        if display_format == "message":
            print(f"The Sum is {results[0]} and Difference is {results[1]}")
        elif display_format == "csv":
            print(f"{results[0]},{results[1]}")
        elif display_format == "json":
            print(f'[{{"Sum":"{results[0]}","Diff":"{results[1]}"}}]')

    @staticmethod
    def input_values():
        """ This function gets to values and returns a sum

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: List of values
        """

        value1 = float(input("Enter the first value: "))
        value2 = float(input("Enter the second value: "))
        return [value1, value2]


''' Main Body of the script '''

# Create a data object
results1 = Results()

# Get the values
values = IO.input_values()

# Process the values
sum = Calculator.add(values[0], values[1])
diff = Calculator.subtract(values[0], values[1])


# Display the results
IO.display_results(results=[sum, diff], display_format='message')
IO.display_results(results=[sum, diff], display_format='csv')
IO.display_results(results=[sum, diff], display_format='json')



