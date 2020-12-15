#!/bin/env python3

from random import choice, randint
from string import ascii_lowercase


def main():
    # Define a list of hardcoded file names to write to, then pass that list to the makeFiles function to create or
    # truncate files with the specified names and write random strings into them. Then, call multiplyTwoNumbers
    # passing minimum and maximum values for random integers to multiply together.
    fileNames = ['file1.txt', 'file2.txt', 'file3.txt']
    minNum = 1
    maxNum = 42

    makeFiles(fileNames)
    multiplyTwoNumbers(minNum, maxNum)


def makeFiles(fileNames):
    # Make a random 10 letter string for each file passed to the function, then open the file, print the string
    # into it and close the file.
    for path in fileNames:
        randomStr = makeString(10)
        print(randomStr)
        file = open(path, 'w')
        print(randomStr, file=file)
        file.close()


def makeString(length):
    # Start with an empty string, then append a random lowercase letter to that string 10 times and return it.
    randomString = ''
    for letter in range(length):
        randomString += choice(ascii_lowercase)
    return randomString


def multiplyTwoNumbers(minNum, maxNum):
    # Store two random integers in the range [minNum, maxNum] into variables. Print out the numbers, followed by their
    # product, all separated by newlines.
    randomOne = randint(minNum, maxNum)
    randomTwo = randint(minNum, maxNum)
    print('%d\n%d\n%d' % (randomOne, randomTwo, randomOne * randomTwo))


if __name__ == "__main__":
    main()
