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

# 
# Initialize macth array with all 0's
matchArr = [0] * 10;

# Count matchs
for i in range(0,numArrLength):

    currEl = numArr[i];
    prevEl = None;
    if (i + 1) != numArrLength:
        prevEl = numArr[i+1];
    else:
        prevEl = numArr[0];

    if currEl == prevEl:
        matchArr[currEl] = matchArr[currEl] + 1;

totalSum = 0;
for i in range(0,10):
    elSum = i*matchArr[i];
    print 'For', i, ', found ', matchArr[i], 'matches; sum =', elSum
    totalSum += elSum;

print 'Total Sum', totalSum
