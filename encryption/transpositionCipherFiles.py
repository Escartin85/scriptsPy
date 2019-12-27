# Transposition Cipher in Files

import time, os, sys, transpositionCipher

def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = 'frankensteinEnrypted.txt'
    myKey = 10
    myMode = 'encrypt'

    # if the input files does not exist, the program terminates early
    if not os.path.exists(inputFilename):
        print('The file %s does not exits. Quitting...' % (inputFilename))
        sys.exit()
    
    # if the output file already exist, give the user a chance to quit
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # measures how long the encryption/decryption takes
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionCipher.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionCipher.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # write out the translated message to the output file
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

if __name__ == '__main__':
    main()

