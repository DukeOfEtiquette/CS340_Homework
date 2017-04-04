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

def getCsvReader(filePath):
  file = open(filePath, 'rb')
  dataReader = csv.reader(file)
  return dataReader

# Helper function to print every row in a csv reader object
def printCsvReader(csvReader):
  for row in csvReader:
    print row

# Open the csv file and get a csv reader object
dataReader = getCsvReader(filePath)

# STEP ONE: Read and Print the data
print "Step 1: Read and Print the data"
printCsvReader(dataReader)

# STEP TWO: Number of Amandas
print "Step 2: Number of Amandas"


