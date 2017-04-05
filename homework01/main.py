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

def getCsvReader(file):
  dataReader = csv.reader(file)
  return dataReader

# Helper function to print every row in a csv reader object
def printCsvReader(csvReader):
  for row in csvReader:
    print row

def numOfAmandas(csvReader):
  # Start counter
  nAmandas = 0

  # Iterate over dataset
  for row in csvReader:
    # If the name field contains 'Amanda' then inc counter
    if row[7].lower().find("amanda") > -1:
      nAmandas += 1

  # Return results
  return nAmandas

def avgTransation(csvReader):
  total = 0
  counter = 0
  # Iterate over dataset
  for row in csvReader:
    if row[2].isdigit():
      total += float(row[2])
      counter += 1

  return total/counter


file = open(filePath, 'rb')
# Open the csv file and get a csv reader object
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
