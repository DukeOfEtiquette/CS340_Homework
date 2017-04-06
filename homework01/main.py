import sys
import csv

# Make sure line argument was passed
if len(sys.argv) != 2:
  print "usage: ./main.py data_file.csv"
  sys.exit(1)

# Store argument locally
filePath = sys.argv[1]

# Print success message with file name
print "Success! File passed:", filePath

# Return a csv reader object based on file path provided
def getCsvReader(file):
  dataReader = csv.reader(file)
  return dataReader

def getKey(item):
  return item[1]

# Helper function to print every row in a csv reader object
# This function and getKey heavily inspired by:
# http://stackoverflow.com/questions/34472390/how-to-sort-data-alphabetically-in-a-csv-file-created-in-python
def printCsvReader(csvReader):
  data = []
  # Move data into a list
  for row in csvReader:
    data.append(row)

  # Sort list based on the Product column
  data.sort(key=getKey)

  # Print each row of list
  for i in data:
    print i

def numOfAmandas(csvReader):
  # Start counter
  nAmandas = 0

  # Iterate over dataset
  for row in csvReader:
    # If the name field contains 'amanda' then inc counter
    if row[7].lower().find("amanda") > -1:
      nAmandas += 1

  # Return results
  return nAmandas

def avgTransation(csvReader):
  total = 0
  counter = 0

  # Iterate over dataset
  for row in csvReader:
    # Make sure it is a digit
    if row[2].isdigit():
      # Add to running total, increment counter
      total += float(row[2])
      counter += 1

  # Return the average
  return total/counter


def replaceUnitedStates(csvReader):
  # Make a copy of our reader
  copyReader = csvReader

  # Open a new csv file and create a write object
  file = open('USA.csv', 'wb')
  writer = csv.writer(file)

  # Start a counter variable
  counter = 0

  # Iterate over reader, making changes as needed
  for row in copyReader:
    if row[6].lower().find("united states") > -1:
      row[6] = "USA"
      counter += 1 # Increment counter

    # Save row to the writer object
    writer.writerow(row)

  file.close() # Close new csv file

  return counter


# Open the csv file and get a csv reader object
file = open(filePath, 'rb')
dataReader = getCsvReader(file)

# STEP ONE: Read and Print the data
print "Step 1: Read and Print the data"
printCsvReader(dataReader)
file.seek(0) # Seek back to start of file

# STEP TWO: Number of Amandas
print "Step 2: Number of Amandas"
print "There are", numOfAmandas(dataReader), "Amandas in this dataset"
file.seek(0) # Seek back to start of file

# STEP THREE: Average Transaction Amount
print "Setp 3: Average Transaction Amount"
print "Avg:", avgTransation(dataReader)
file.seek(0) # Seek back to start of file

# STEP FOUR: USA! USA! USA!
print "Step 4: USA! USA! USA!"
print replaceUnitedStates(dataReader), "records changed to USA"
file.seek(0) # Seek back to start of file

file.close() # Close it up
