# Transposition Cipher Test

import random, sys, transpositionCipher

def main():
    # set the random seed to a static value
    random.seed(42)

    for count in range(20):
        # generate random messages to test
        # the message will have a random lenght:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' * random.randint(4, 40)

        # convert the message string to a list to shiffle it:
        message = list(message)
        random.shuffle(message)
        # convert the list back to a string
        message = ''.join(message)

        print('Test #%s: "%s"' % (count + 1, message[:50]))

        # check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionCipher.encryptMessage(key, message)
            decrypted = transpositionCipher.decryptMessage(key, encrypted)

            # if the decryption doesn't match the original message, display
            # an error message and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()