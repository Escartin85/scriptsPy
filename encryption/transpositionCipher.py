# Transposition cipher

import math

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 18

    ciphertext = encryptMessage(myKey, myMessage)

    # print the encrypted string in chipertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # then end of the encrypted message:
    print(ciphertext + '|')
    print()
    text = decryptMessage(myKey, ciphertext)
    print(text + '|')

def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key
    # print(ciphertext)
    # loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # move currentIndex over:
            currentIndex += key
    
    # convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

def decryptMessage(key, message):
    # the transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # the number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key))) 
    # tje number of "rows" in our grid
    numOfRows = key
    # the number of "shaded boxes" in the last "column" of the grid
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # each string in plaintext represents a column in the grid:
    plaintext = [''] * numOfColumns

    # the column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        # point to the next column
        column += 1 

        # if there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row:
        if(column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    
    return ''.join(plaintext)

# if is run (instead of imported as a module) call the main function
if __name__ == '__main__':
    main()