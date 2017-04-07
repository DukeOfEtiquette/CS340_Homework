'''

Author: Adam DuQuette
Creation: April 5, 2017

Description:

This program was written for Homework 1, CS340 - Intro To Databases, Spring 2017
Oregon Status University - Cascades.

This program takes a csv file as a parameter and performs set operations on it's
data.

'''

import sys
import csv

# Make sure line argument was passed
if len(sys.argv) != 2:
    print "usage: ./main.py data_file.csv"
    sys.exit(1)

# Store argument locally
file_path = sys.argv[1]

# Print success message with file name
print "Success! File passed:", file_path


# Return a csv reader object based on file path provided
def get_csv_reader(csv_file):
    data_reader = csv.reader(csv_file)
    return data_reader


def get_key(item):
    return item[1]


# Helper function to print every row in a csv reader object
# This function and getKey heavily inspired by:
# http://stackoverflow.com/questions/34472390/how-to-sort-data-alphabetically-in-a-csv-file-created-in-python
def print_csv_reader(csv_reader):
    data = []
    # Move data into a list
    for row in csv_reader:
        data.append(row)

    # Sort list based on the Product column
    data.sort(key=get_key)

    # Print each row of list
    for i in data:
        print i


def num_of_amandas(csv_reader):
    # Start counter
    nAmandas = 0

    # Iterate over dataset
    for row in csv_reader:
        # If the name field contains 'amanda' then inc counter
        if row[7].lower().find("amanda") > -1:
            nAmandas += 1

    # Return results
    return nAmandas


def avg_transaction(csv_reader):
    total = 0
    counter = 0

    # Iterate over dataset
    for row in csv_reader:
        # Make sure it is a digit
        if row[2].isdigit():
            # Add to running total, increment counter
            total += float(row[2])
            counter += 1

    # Return the average
    return total/counter


def replace_united_states(csv_reader):
    # Make a copy of our reader
    copy_reader = csv_reader

    # Open a new csv file and create a write object
    file = open('USA.csv', 'wb')
    writer = csv.writer(file)

    # Start a counter variable
    counter = 0

    # Iterate over reader, making changes as needed
    for row in copy_reader:
        if row[6].lower().find("united states") > -1:
            row[6] = "USA"
            counter += 1 # Increment counter

    # Save row to the writer object
    writer.writerow(row)

    file.close()  # Close new csv file

    return counter


# Open the csv file and get a csv reader object
file = open(file_path, 'rb')
data_reader = get_csv_reader(file)

# STEP ONE: Read and Print the data
print "Step 1: Read and Print the data"
print_csv_reader(data_reader)
file.seek(0)  # Seek back to start of file

# STEP TWO: Number of Amandas
print "Step 2: Number of Amandas"
print "There are", num_of_amandas(data_reader), "Amandas in this dataset"
file.seek(0)  # Seek back to start of file

# STEP THREE: Average Transaction Amount
print "Setp 3: Average Transaction Amount"
print "Avg:", avg_transaction(data_reader)
file.seek(0)  # Seek back to start of file

# STEP FOUR: USA! USA! USA!
print "Step 4: USA! USA! USA!"
print replace_united_states(data_reader), "records changed to USA"
file.seek(0)  # Seek back to start of file

file.close()  # Close it up
