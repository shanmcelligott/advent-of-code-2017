#!/usr/bin/python

import sys

# Check arguments
if len(sys.argv) < 2:
    print 'Provide a number.'
    exit();

# Convert input into a number
numberString = sys.argv[1];
endNumber = int(numberString);

RIGHT_INDEX = 0;
UP_INDEX = 1;
LEFT_INDEX = 2;
DOWN_INDEX = 3;

# Current number we are looking at
currentNumber = 1;
# Steps array: [0] = R, [1] = U, [2] = L, [3] = D
stepsArray = [0, 0, 0, 0];
# Number of steps needed in one direction
numStepsLeft = 1;
nextNumStepsLeft = 1;
# Index of the steps array
directionIndex = 0;

while (currentNumber != endNumber):
    currentNumber = currentNumber + 1;
    stepsArray[directionIndex] = stepsArray[directionIndex] + 1;
    numStepsLeft = numStepsLeft - 1;

    if (numStepsLeft == 0):
        if directionIndex == RIGHT_INDEX or directionIndex == LEFT_INDEX:
            numStepsLeft = nextNumStepsLeft;
            nextNumStepsLeft = nextNumStepsLeft + 1;
        else:
            numStepsLeft = nextNumStepsLeft;
        directionIndex = (directionIndex + 1) % len(stepsArray);
    


# Calculating the total number of steps
numVerticalSteps = stepsArray[UP_INDEX] - stepsArray[DOWN_INDEX];
if (numVerticalSteps < 0):
    numVerticalSteps = numVerticalSteps * -1;

numHorizontalSteps = stepsArray[RIGHT_INDEX] - stepsArray[LEFT_INDEX];
if (numHorizontalSteps < 0):
    numHorizontalSteps = numHorizontalSteps * -1;

totalSteps = numVerticalSteps + numHorizontalSteps;

print 'Total Steps', totalSteps
