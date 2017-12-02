#!/usr/bin/python

import sys

# Check arguments
if len(sys.argv) < 2:
    print 'Provide a file name.'
    exit();

# Get file name and read in file
fileName = sys.argv[1];
fileContents = None;
with open(fileName, 'r') as fileObj:
    fileContents = fileObj.read().rstrip();

# Convert file contents into an array of numbers
numArr = [];
for x in fileContents:
    numArr.append(int(x))
numArrLength = len(numArr);

# Count matches
totalSum = 0;
for currElIndex in range(0,numArrLength/2):

    if numArr[currElIndex] == numArr[currElIndex + numArrLength/2]:
        totalSum += 2*numArr[currElIndex];

print 'Total Sum', totalSum
