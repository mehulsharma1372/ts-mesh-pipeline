"""This is the main file responsible for calling all the classes and functions. I have taken 10 values for the demonstration, getting a for loop can easily give all. """

from dependencies.standardization.standardizer import CsvOperations


if __name__ == "__main__":
    csv = CsvOperations()
    csv.to_csv()
