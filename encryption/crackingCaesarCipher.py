# Caesar Cipher

# the string to be encrypted/decrypted
#message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
message = 'qeFIP?eGSeECNNS'

# the encryption/descryption key:
key = ''

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# loop through every possible key:
for key in range(len(SYMBOLS)):
    # it is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''
        
    for symbol in message:
        # Only symbols in the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            # handle wraparound, if needed:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            # append the decrypted symbol
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # append the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))